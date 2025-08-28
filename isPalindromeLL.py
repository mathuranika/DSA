'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        length = 0
        curr = head
        
        while curr:
            length+=1
            curr = curr.next
            
        mid = (length//2) + 1
            
        curr = head
        stack = [None]
        count = 0
        
        while curr:
            count += 1
            if count < mid:
                stack.append(curr.data)
            
            elif length%2 != 0 and count == mid:
                curr = curr.next
                continue
            
            else:
                if stack[-1] != curr.data:
                    return False
                else:
                    stack.pop()
                    
            curr = curr.next
                    
        return True
            
        
            
        
        
