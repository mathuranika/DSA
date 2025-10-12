#User function Template for python3

class Solution:
    def findMin(self, arr):
        n = len(arr)
        l,h=0,n-1
        res = float('inf')
        
        while l<=h:
            m = (l+h)//2
            if arr[m]>=arr[l]:
                res = min(res,arr[l])
                l=m+1
            else:
                res = min(res,arr[m])
                h = m-1
                
        return res
                
