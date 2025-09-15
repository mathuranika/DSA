class Solution:
    def maxSubarraySum(self, arr):
        n =len(arr)
        max_sum = float('-inf')
        curr_sum = 0
        for i in range(n):
            curr_sum += arr[i]
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
