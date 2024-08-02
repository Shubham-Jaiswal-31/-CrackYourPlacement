class Solution:
    def subLinkedList(self, l1, l2): 
        cur = l1
        n1 = 0
        while cur:
            n1 *= 10
            n1 += cur.data
            cur = cur.next
        
        n2 = 0
        cur = l2
        while cur:
            n2 *= 10
            n2 += cur.data
            cur = cur.next
        
        sub = str(abs(n1 - n2))
        
        dummy = Node(0)
        cur = dummy
        for c in sub:
            cur.next = Node(int(c))
            cur = cur.next
        
        return dummy.next
