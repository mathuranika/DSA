#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            res+=s[len(s)-i-1]
            
        return res
