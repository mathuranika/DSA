class Solution:
    def rearrange(self, arr):
        arr.sort()
        n = len(arr)
        i = 0
        j = n-1
        
        while i<j:
            temp = arr[j]
            arr.insert(i,temp)
            arr.pop()
            i+= 2
            
        return arr
