class Solution:
    def isSparse(self,n):
        return (n & (n >> 1)) == 0
