'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        length = 0
        curr = head
        while curr!= None:
            length += 1
            curr = curr.next
            
        if k>length:
            return -1
            
        curr = head
        lim = length-k
        count = 0
        
        while count < lim:
            count += 1
            curr = curr.next
            
        return curr.data
