#User function Template for python3

class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [0]*(n+1)
        i = 1
        
        while i <= n:
            for j in range(0,i):
                dp[i] = max(dp[i],price[j]+dp[i-j-1])
            i+=1
                
        return dp[n]
                
            
        
