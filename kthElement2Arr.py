class Solution:
    def kthElement(self, a, b, k):
       new = a + b
       new.sort()
       return new[k-1]
