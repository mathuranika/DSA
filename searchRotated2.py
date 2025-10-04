class Solution:
    def search(self, arr, key):
        n = len(arr)
        low,high = 0, n-1
        
        while low <= high:
            mid = (low+high) //2
            if arr[mid] == key:
                return True
            if arr[low]==arr[mid]==arr[high]:
                low+=1
                high-=1
                continue
        
            if arr[low]<=arr[mid]:
                if arr[low]<=key and arr[mid]>=key:
                    high = mid-1
                else:
                    low = mid+1
                    
            else:
                if arr[mid]<=key and arr[high]>=key:
                    low = mid+1
                else:
                    high = mid-1
                
        return False
