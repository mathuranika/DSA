'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        
        # If list is empty
        if head is None:
            return new_node
        
        # Traverse to the end
        temp = head
        while temp.next is not None:
            temp = temp.next
        
        # Insert new node
        temp.next = new_node
        return head
