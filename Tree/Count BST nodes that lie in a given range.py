#Function to count number of nodes in BST that lie in the given range.
class Solution:
    def check(self,root,count,low,high):
        if root is None:
            return 0
        if root.data >= low and root.data <= high:
            count[0] += 1
        self.check(root.left,count,low,high)
        self.check(root.right,count,low,high)
        
        
    def getCount(self,root,low,high):
        count = [0]
        self.check(root,count,low,high)
        return count[0]
