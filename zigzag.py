
from typing import List


class Solution:
    def zigZag(self,arr : List[int]) -> None:
        turn = "<"
        mod = arr
        n = len(mod)
        
        if n == 1:
            return arr
            
        for i in range(0,n-1):
            if turn == "<":
                if mod[i]>mod[i+1]:
                   mod[i],mod[i+1] = mod[i+1],mod[i]
                turn = ">"
               
            else:
                if mod[i]<mod[i+1]:
                   mod[i],mod[i+1] = mod[i+1],mod[i]
                turn = "<"
               
        
        return mod
               
            
        
        
