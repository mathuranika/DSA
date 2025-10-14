class Solution:
    def findUnion(self, a, b):
        res = []
        n = len(a)
        m = len(b)
        
        i = 0
        j = 0
        
        while i < n and j < m:
            if a[i] <= b[j]:
                if not res or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
            else:
                if not res or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
                
        while i < n:
            if not res or res[-1] != a[i]:
                res.append(a[i])
            i += 1
        
        while j < m:
            if not res or res[-1] != b[j]:
                res.append(b[j])
            j += 1
        
        return res
