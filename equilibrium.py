# User function Template for python3

class Solution:
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        
        for i, num in enumerate(arr):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i  
            left_sum += num
        
        return -1
