"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        length = 0
        a = head
        
        while a:
            length += 1
            a = a.next
            
        if length == 1:
            return head
            
        new_head = head.next
        
        prev = head
        last = None   

        while prev and prev.next:
            curr = prev.next
            prev.next = curr.next
            curr.next = prev

            if last:         
                last.next = curr

            last = prev      
            prev = prev.next 
            
        return new_head
