class Solution:
    def single(self, arr):
        i = 0
        n = len(arr)
        while i< n:
            if i == n-1:
                return arr[i]
            if arr[i]!= arr[i+1]:
                return arr[i]
            i+=2
        
        
