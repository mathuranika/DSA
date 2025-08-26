"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def reverseList(self, head):
        prev = None 
        current = head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
        
        
