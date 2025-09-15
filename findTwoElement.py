class Solution:
    def findTwoElement(self, arr):
        res = []
        prev = -1
        find = 1
        i = 0
        arr.sort()
        n = len(arr)
        
        while i < n:
            if arr[i] == prev:
                res.append(arr[i])   
            else:
                prev = arr[i]
            i += 1
        
        for i in range(n):
            if arr[i] > find:
                res.append(find)     
                break
            elif arr[i] == find:
                find += 1
        
        if len(res) == 1:
            res.append(find)
                
        return res
