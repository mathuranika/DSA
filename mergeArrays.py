class Solution:
    def mergeArrays(self, a, b):
        n = len(a)   
        j = 0
        for i in range(len(b)):
            x = b[i]
            while j < len(a) and a[j] <= x:
                j += 1
            a.insert(j, x)
            j += 1  

        b[:] = a[n:]   
        del a[n:]     
