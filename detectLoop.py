'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return True   
            visited.add(current)
            current = current.next
        
        return False  

        
        
