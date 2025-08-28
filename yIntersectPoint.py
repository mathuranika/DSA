'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        h1_trav = set()
        res = None
        
        curr1 = head1
        
        while curr1:
            h1_trav.add(curr1)
            curr1 = curr1.next
            
        curr2 = head2
        
        while curr2:
            if curr2 in h1_trav:
                res = curr2
                break
            curr2 = curr2.next
        
        return res
