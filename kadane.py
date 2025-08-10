class Solution:
    def maxSubarraySum(self, arr):
        current_sum = max_sum = arr[0]
    
        for x in arr[1:]:
            current_sum = max(x, current_sum + x)
            max_sum = max(max_sum, current_sum)
        
        return max_sum
