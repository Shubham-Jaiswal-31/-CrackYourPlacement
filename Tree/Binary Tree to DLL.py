'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    final = None
    temp = None
    def bToDLL(self,root):
        if root:
            self.bToDLL(root.left)
            if self.final==None:
                self.final=Node(root.data)
                self.temp=self.final
            else:
                curr=self.temp
                self.temp.right=Node(root.data)
                self.temp=self.temp.right
                self.temp.left=curr
            self.bToDLL(root.right)
        return self.final

