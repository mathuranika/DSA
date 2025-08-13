from collections import Counter

class Solution:
    def findMajority(self, arr):
        counts = Counter(arr)
        res = []
        k = len(arr)//3
        for item in counts.keys():
            if counts[item]>k:
                res.append(item)
                
        res.sort()
        return res
                
