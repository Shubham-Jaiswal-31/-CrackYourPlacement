'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#return: minimum distance between a and b in a tree with given root
class Solution:
    def findDist(self,root,a,b):
        lca = self.lowestCommonAncestor(root, a, b)
        d1 = self.disrFromLCA(lca, a, 0)
        d2 = self.disrFromLCA(lca, b, 0)
        return (d1 + d2)
    
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None 

        if root.data == p or root.data == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l if l else r
    
    def disrFromLCA(self, root, k, dist):
        if not root:
            return -1
        if root.data == k:
            return dist
        
        l = self.disrFromLCA(root.left, k, dist + 1)
        if l != -1:
            return l
        return self.disrFromLCA(root.right, k, dist + 1)