class Solution:
    def reverseArray(self, arr):
       n = len(arr)
       low = 0
       high = n-1
       while low<=high:
           arr[low],arr[high]=arr[high],arr[low]
           low += 1
           high -= 1
       return arr
