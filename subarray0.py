class Solution:
    def maxLength(self, arr):
        n = len(arr)
        prefix_sum = 0
        res = 0
        seen = {}   # stores first occurrence of a prefix sum
        
        for i in range(n):
            prefix_sum += arr[i]
            
            if prefix_sum == 0:   # whole array till i has sum 0
                res = max(res, i + 1)
                
            if prefix_sum in seen:
                res = max(res, i - seen[prefix_sum])
            else:
                seen[prefix_sum] = i  # store only first occurrence
                
        return res
