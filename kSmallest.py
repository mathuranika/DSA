class Solution:

    def kthSmallest(self, arr,k):
        max_val = max(arr)
        freq = [0] * (max_val + 1)
        
        for num in arr:
            freq[num] += 1
        
        count = 0
        for num in range(len(freq)):
            count += freq[num]
            if count >= k:
                return num
