#User function Template for python3

class Solution:
    def find(self, arr, x):
        n = len(arr)
        low = 0
        high = n-1
        first = -1
        
        while low <= high:
            mid = (low+high)//2
            
            if arr[mid] > x:
                high = mid-1
            elif arr[mid] == x:
                first = mid
                high = mid-1
            else:
                low = mid+1
        
        if first == -1:
            return [-1,-1]
            
        last = -1
        i = first + 1
        
        while i<n and arr[i]==x:
            i+=1
            
        last = i - 1
        
        return [first,last]
            
