'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    def removeLoop(self, head):
        seen = set()
        
        prev = head
        curr = prev.next
        seen.add(prev)
        
        while curr!=None:
            if curr in seen:
                prev.next = None
                break
            seen.add(curr)
            prev = curr
            curr = curr.next
        return head
            
