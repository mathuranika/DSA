class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        arr.sort()
        arr_sum = sum(arr)
        mult = n+1
        exp = n*mult/2
        res = exp-arr_sum
        return int(res)
