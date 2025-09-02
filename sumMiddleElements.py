#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        arr = arr1 + arr2
        arr.sort()
        n = len(arr)
        return arr[n//2] + arr[(n//2)-1]
