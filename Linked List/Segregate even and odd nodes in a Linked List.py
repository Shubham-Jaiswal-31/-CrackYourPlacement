# Following is the structure of node 
# class node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, head):
        cur = head
        dummy1 = node()
        odd = dummy1
        dummy2 = node()
        even = dummy2
        
        while cur:
            if cur.data % 2:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
        
        even.next = dummy1.next
        odd.next = None
        return dummy2.next