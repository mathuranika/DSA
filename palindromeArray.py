
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        n = len(arr)//2
        
        i=0
        
        while i<n:
            if arr[i]==arr[-i-1]:
                i+=1
            else:
                return False
                
        return True
        
