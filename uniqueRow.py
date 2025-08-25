from typing import List

class Solution:
    def uniqueRow(self, row : int, col : int, M : List[List[int]]) -> List[List[int]]:
        unq = []
        seen = []
        for r in range(row):
            row_str = str(M[r])
            if row_str not in seen:
                seen.append(row_str)
                unq.append(M[r])
        return unq
                
