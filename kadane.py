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

#Leetcode

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        max_sum = float("-inf")
        n = len(nums)
        for i in range(0,n):
            curr += nums[i]
            max_sum = max(curr,max_sum)
            if curr<0:
                curr = 0

        return max_sum
        
