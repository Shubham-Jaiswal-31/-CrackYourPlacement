'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None     
'''
class Solution:
    def flatten(self, root):
        if not root or not root.next:
            return root
        mergedHead = self.flatten(root.next)
        return self.merge2lists(root, mergedHead)
        
    def merge2lists(self, l1, l2):
        dummy = Node(-1)
        res = dummy
        
        while l1 and l2:
            if l1.data < l2.data:
                res.bottom = l1
                res = l1
                l1 = l1.bottom
            else:
                res.bottom = l2
                res = l2
                l2 = l2.bottom
            res.next = None
        if l1:
            res.bottom = l1
        elif l2:
            res.bottom = l2
        return dummy.bottom