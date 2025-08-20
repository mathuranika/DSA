#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):
        arr.sort()
        n = len(arr)
        i = 0
        j = M-1
        mini = arr[j]-arr[i]
        
        while j<n:
            diff = arr[j]-arr[i]
            mini = min(mini,diff)
            i+=1
            j+=1
        
        return mini
