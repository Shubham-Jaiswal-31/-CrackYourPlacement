'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:
    def findPreSuc(self, root, pre, suc, key):
        cur = root
        while cur:
            if key >= cur.key:
                cur = cur.right
            else:
                suc.key = cur.key
                cur = cur.left
                
        cur = root
        while cur:
            if key <= cur.key:
                cur = cur.left
            else:
                pre.key = cur.key
                cur = cur.right
        return