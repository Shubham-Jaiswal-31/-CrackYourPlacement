class Solution:
    def isDeadEnd(self, root):
        # Code here
        def dfs(root, l, r):
            if not root:
                return False
            if l == r:
                return True
            return dfs(root.left, l, root.data - 1) or dfs(root.right, root.data + 1, r)
    
        return dfs(root, 1, float('inf'))