class Solution:
    def countBitsFlip(self, a, b):
        bin_a = str(bin(a))[2:]
        bin_b = str(bin(b))[2:]
        res = 0
        na = len(bin_a)
        nb = len(bin_b)
        
        if na>nb:
            diff = na-nb
            bin_b = "0"*diff + bin_b
            
        elif nb>na:
            diff = nb-na
            bin_a = "0"*diff +bin_a
            
        n = len(bin_a)
        
        for i in range(n):
            if bin_a[i]!=bin_b[i]:
                res+=1
                
        return res
