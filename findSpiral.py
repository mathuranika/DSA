'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''        

class Solution:
    def findSpiral(self, root):
        
        level = 1
        res = []
        queue = [root]
        
        while queue:
            new_lev = []
            curr_level = []
            
            while queue:
                node = queue.pop(0)
                curr_level.append(node.data)
                
                if node.left:
                    new_lev.append(node.left)
                if node.right:
                    new_lev.append(node.right)
            
            if level % 2 == 1:  
                res.extend(curr_level[::-1])
            else:                
                res.extend(curr_level)
            
            queue = new_lev
            level += 1
        
        return res

                    
                
                
