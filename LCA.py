##Binary Tree
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def LCA(self, root, n1, n2):
        if not root:
            return
        if n1.data > root.data and n2.data> root.data:
            return self.LCA(root.right, n1, n2)
        elif n1.data < root.data and n2.data < root.data:
            return self.LCA(root.left, n1, n2)
        else:
            return root
    
