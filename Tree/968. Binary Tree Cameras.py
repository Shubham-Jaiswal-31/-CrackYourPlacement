# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 1
            l, r = dfs(root.left), dfs(root.right)
            if l == -1 or r == -1:
                self.res += 1
                return 0
            return 1 if l == 0 or r == 0 else -1

        return (dfs(root) == -1) + self.res