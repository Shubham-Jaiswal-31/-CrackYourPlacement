# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, 0, len(preorder) - 1, postorder, 0, len(postorder) - 1)

    def dfs(self, pre, preL, preR, post, postL, postR):
        if preL > preR:
            return None
        
        root = TreeNode(pre[preL])
        if preL == preR:
            return root
        
        postIdx = postL
        while post[postIdx] != pre[preL + 1]:
            postIdx += 1
        
        length = postIdx - postL + 1
        root.left = self.dfs(pre, preL + 1, preL + length, post, postL, postIdx)
        root.right = self.dfs(pre, preL + length + 1, preR, post, postIdx + 1, postR - 1)

        return root