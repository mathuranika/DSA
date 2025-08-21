#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        na = len(A)
        nb = len(B)
        
        queue = list(A)
        
        for i in B:
            if len(queue) == 0:
                break
            if i==queue[0]:
                queue.pop(0)
                
        if len(queue) == 0:
            return True
        
        return False
