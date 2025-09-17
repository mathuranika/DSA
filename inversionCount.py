class Solution:
    
    def merge(self, arr, l, m, r):
        res = 0
        temp = []
        left = l
        right = m + 1
        
        while left <= m and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                res += m + 1 - left
                right += 1
                
        while left <= m:
            temp.append(arr[left])
            left += 1
            
        while right <= r:
            temp.append(arr[right])
            right += 1  
        
        for i in range(l, r+1):
            arr[i] = temp[i-l]
            
        return res

    def mergeSort(self, arr, l, r):
        res = 0
        if l < r:  
            m = (l + r) // 2
            res += self.mergeSort(arr, l, m)
            res += self.mergeSort(arr, m+1, r)
            res += self.merge(arr, l, m, r)
        return res
        
    def inversionCount(self, arr):
        n = len(arr)
        return self.mergeSort(arr,0,n-1)
        
        
