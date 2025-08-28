class Solution:
    def romanToDecimal(self, s): 
        r2d = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        val = 0
        n = len(s)
        
        if n == 1:
            return r2d[s]
        
        i = 0
        while i<n:
            curr = s[i]
            if i+1<n:
                nxt = s[i+1]
                if r2d[curr]<r2d[nxt]:
                    val += r2d[nxt]-r2d[curr]
                    i+=2
                else:
                    val+= r2d[curr]
                    i+=1
            else:
                val += r2d[curr]
                i+=1
        
        return val
