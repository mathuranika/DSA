'''
    :param x: value to be inserted
    :return: None
'''
from queue import Queue   
   
def push(x):
    
    global queue_1
    global queue_2
    queue_1.put(x)

def pop():
    
    global queue_1
    global queue_2
    
    if queue_1.empty():
        return -1
    while queue_1.qsize()>1:
        queue_2.put(queue_1.get())
    popped=queue_1.get()
    queue_1,queue_2=queue_2,queue_1
    return popped
