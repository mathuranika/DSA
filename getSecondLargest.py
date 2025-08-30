class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        n = len(arr)
        i = -2
        while i>-n and arr[i] == arr[i+1]:
            i -= 1
            
        if i == -n and arr[i] == arr[-1]:
            return -1
            
        return arr[i]
