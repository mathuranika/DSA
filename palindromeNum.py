class Solution:
    def isPalindrome(self, n):
		str_n = str(n)
		k = len(str_n)//2
		
		i=0
        
        while i<k:
            if str_n[i]==str_n[-i-1]:
                i+=1
            else:
                return False
                
        return True
