# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        
        def sum2(root, target):
            if not root:
                return 0
            res = 0
            if root.val == target:
                res += 1
            res += sum2(root.left, target - root.val)
            res += sum2(root.right, target - root.val)
            return res
        
        if not root:
            return 0
        return self.pathSum(root.left, target) + sum2(root, target) + self.pathSum(root.right, target)