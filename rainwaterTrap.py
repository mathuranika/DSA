
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        l = 0
        r = n-1
        maxl = 0
        maxr = 0
        water = 0
        
        while l<r:
            if arr[l]<arr[r]:
                if arr[l]>=maxl:
                    maxl = arr[l]
                else:
                    water += maxl-arr[l]
                    
                l+=1
            else:
                if arr[r]>=maxr:
                    maxr = arr[r]
                else:
                    water += maxr-arr[r]
                    
                r-=1
            
        return water
