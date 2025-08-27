'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        curr = head
        length = 0
        
        while curr!=None:
            length+=1
            curr = curr.next
            
        mid = (length//2) + 1
        
        count = 1
        curr = head
        
        while count<mid:
            curr = curr.next
            count += 1
            
        return curr.data
        
