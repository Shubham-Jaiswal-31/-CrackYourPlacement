'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def sumK(self,root,k):
        path = []
        res = 0
        
        def dfs(root, path, k):
            if not root:
                return
        
            path.append(root.data)
            dfs(root.left, path, k)
            dfs(root.right, path, k)
            f = 0
            nonlocal res
            for j in range(len(path) - 1, -1, -1):
                f += path[j]
                if f == k:
                    res += 1
            path.pop()
        
        dfs(root, path, k)
        return res
