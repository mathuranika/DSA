#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        n = len(arr1)
        arr1.sort()
        arr1.reverse()
        arr2.sort()
        res = 0
        for i in range(0,n):
            res+=arr1[i]*arr2[i]
        return res
