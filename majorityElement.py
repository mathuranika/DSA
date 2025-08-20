from collections import Counter

class Solution:
    def majorityElement(self, arr):
        arr_count = Counter(arr)
        max_count_key = max(arr_count, key=arr_count.get)
        if arr_count[max_count_key] > len(arr) // 2:
            return max_count_key
        return -1
