class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize

class Solution:
    def largestBst(self, root):
        return self.dfs(root).maxSize
    
    def dfs(self, root):
        if not root:
            return NodeValue(float('inf'), float('-inf'), 0)
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if left.maxNode < root.data < right.minNode:
            return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), 
            left.maxSize + right.maxSize + 1)
        
        return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))

