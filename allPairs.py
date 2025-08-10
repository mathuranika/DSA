#User function Template for python3
from collections import Counter

class Solution:
    def allPairs(self, target, arr1, arr2):
        c1 = Counter(arr1)
        c2 = Counter(arr2)
        pairs = []
        
        for a in sorted(c1.keys()):
            b = target - a
            if b in c2:
                mult= c1[a] * c2[b]
                pairs.extend([(a, b)] * mult)
        return pairs
