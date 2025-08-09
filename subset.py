from collections import Counter

class Solution:
    def isSubset(self, a, b):
        a_count = Counter(a)
        b_count = Counter(b)
        for key in b_count:
            if b_count[key] > a_count.get(key, 0):
                return False
        return True
