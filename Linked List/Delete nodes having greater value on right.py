'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def rev(self, root):
        prev, cur = None, root
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
        
    def compute(self,head):
        head = self.rev(head)
        cur = head
        ma = head.data
        prev = head
        head = head.next
        while head:
            if head.data >= ma:
                ma = head.data
                prev = head
                head = head.next
            else:
                prev.next = head.next
                head = prev.next
        head = self.rev(cur)
        return head
