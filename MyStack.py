class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    #Function to push an integer into the stack.
    
    def __init__(self):
        self.head=None
        
    def push(self, data):
        new = StackNode(data)
        curr = self.head
        if curr == None:
            self.head = new
            return self.head
        
        while curr.next!=None:
            curr = curr.next
        
        curr.next = new
        return self.head
        
        


    #Function to remove an item from top of the stack.
    def pop(self):
        if self.head == None:
            return -1
        if not self.head.next:
            ele=self.head.data
            self.head=None
            return ele
            
        prev=self.head
        curr = prev.next
        
        while curr.next!=None:
            prev = curr
            curr = curr.next
            
        ele = curr.data
        prev.next = None
        
        return ele
