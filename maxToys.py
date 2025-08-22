#User function Template for python3

class Solution:
    def toyCount(self, N, K, arr):
        arr.sort()
        i = 0
        res = 0
        
        while i<N and K>=arr[i]:
            K -= arr[i]
            res += 1
            i+=1
            
        return res
            
            
