'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def rotate(self, head, k):
        if not head or not head.next or k == 0:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        tail.next = head

        new_tail = head
        for _ in range(k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        new_tail.next = None
        return new_head
