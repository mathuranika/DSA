#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        if not arr:
            return ""
        
        arr.sort()
        first = arr[0]
        last = arr[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        
        return first[:i]
