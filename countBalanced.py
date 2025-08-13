class Solution:
    def countBalanced(self, arr):
        # code here
        idx ={0:1}
        vo = ['a','e','i','o','u']
        total =0
        ans = 0
        for i in arr:
            curr = 0
            for j in i:
                if j in vo:
                    curr+=1
                else:
                    curr-=1
            
            total += curr
            if total in idx:
                ans+= idx[total]
            idx[total] =idx.setdefault(total,0) +1
        return ans
            
            
        
