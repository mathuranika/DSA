#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        seen = []
        
        for i in s:
            if i in seen:
                return i
            else:
                seen.append(i)
        
        return -1
