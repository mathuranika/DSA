class Solution:
    def count(self, coins, sum):
        dp = [0]*(sum+1)
        dp[0] = 1
        
        for coin in coins:
            for amt in range(coin,sum+1):
                dp[amt] += dp[amt-coin]
        
        return dp[sum]
