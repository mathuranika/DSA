'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def deleteNode(self, head, x):
        if x == 1:
            return head.next
            
        cnt = 1
        prev = head
        curr = head.next
        
        while curr and cnt < x:
            if cnt == x-1:
                prev.next = curr.next
            else:
                prev=curr
                curr=curr.next
                
            cnt+=1
            
        return head
