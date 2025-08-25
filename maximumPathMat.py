class Solution:
    def maximumPath(self, mat):
        # DP table same size as matrix
        n = len(mat)
        m = len(mat[0])
        dp = [[0] * m for _ in range(n)]
        
        # Base case: first row
        for j in range(m):
            dp[0][j] = mat[0][j]
        
        # Fill DP table row by row
        for i in range(1, n):
            for j in range(m):
                up = dp[i-1][j]
                up_left = dp[i-1][j-1] if j-1 >= 0 else 0
                up_right = dp[i-1][j+1] if j+1 < m else 0
                
                dp[i][j] = mat[i][j] + max(up, up_left, up_right)
        
        # Answer is max in last row
        return max(dp[n-1])
