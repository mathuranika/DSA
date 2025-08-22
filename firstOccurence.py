class Solution:
    def firstOccurence(self,txt,pat):
        start = 0
        end = len(pat)-1
        
        while end < len(txt):
            if txt[start:end+1] == pat:
                return start
            start += 1
            end += 1
        
        return -1
