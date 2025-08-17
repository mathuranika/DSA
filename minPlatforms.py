#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        n = len(arr)
        arr.sort()
        dep.sort()
        platforms_needed = 0
        max_platforms = 0
        i,j =0,0
        
        while i < n and j < n:
            if arrival[i] <= departure[j]:
                platforms_needed += 1
                max_platforms = max(max_platforms, platforms_needed)
                i += 1
            else:
                platforms_needed -= 1
                j += 1

        return max_platforms
