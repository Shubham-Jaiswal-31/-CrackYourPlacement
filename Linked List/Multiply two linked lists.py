'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        MOD = 10 ** 9 + 7
        n1, n2 = 0, 0
        cur = first
        while cur:
            n1 = (n1 * 10 + cur.data) % MOD
            cur = cur.next
        
        cur = second
        while cur:
            n2 = (n2 * 10 + cur.data) % MOD
            cur = cur.next
        
        return (n1 * n2) % MOD