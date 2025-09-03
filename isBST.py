'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        queue = [(root, float('-inf'), float('inf'))]   # store (node, min, max)
        
        while queue:
            node, low, high = queue.pop(0)
            
            if not (low < node.data < high):
                return False
            
            if node.left:
                queue.append((node.left, low, node.data))
            if node.right:
                queue.append((node.right, node.data, high))
                    
        return True
