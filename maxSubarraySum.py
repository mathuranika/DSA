class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        
        if k == n:
            return sum(arr)
        if k == 1:
            return max(arr)
        
        first = 0
        last = k
        
        curr_sum = max_sum = sum(arr[first:last])
        
        first += 1
        last += 1
        
        while last<=n:
            curr_sum -= arr[first-1]
            curr_sum += arr[last-1]
            max_sum = max(curr_sum,max_sum)
            first+=1
            last+=1
        
        return max_sum
        
