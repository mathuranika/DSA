from collections import Counter
class Solution:
    def areAnagrams(self, s1, s2):
       s1_count = Counter(s1)
       s2_count = Counter(s2)
       
       if s1_count == s2_count:
           return True
       return False
       
       
    
       
