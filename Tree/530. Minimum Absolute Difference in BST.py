# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node, low, high):
            if not node:
                return high - low
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            return min(left, right)

        return dfs(root, float('-inf'), float('inf'))