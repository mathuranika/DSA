class Solution:
    def subarrayXor(self, arr, k):
        n = len(arr)
        xr = 0
        seen = {0:1}
        res = 0
        
        for i in range(n):
            xr = xr^arr[i]
            x = xr^k
            
            if x in seen.keys():
                res += seen[x]
            if xr in seen.keys():
                seen[xr] += 1
            else:
                seen[xr] = 1
            
        return res
