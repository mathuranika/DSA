'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
class Solution:
    def countLeaves(self, root):
        if root is None:
            return 0   

        queue = [root]
        res = 0
       
        while queue:   
            node = queue.pop(0)

            if node.left is None and node.right is None:
                res += 1
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
           
        return res
