class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size) -> Node:
    i = 0
    def build(pre, bound):
        nonlocal i
        if i == size or pre[i] > bound:
            return None
        root = Node(pre[i])
        i += 1
        root.left = build(pre, root.data)
        root.right = build(pre, bound)
        return root
        
    return build(pre, float('inf'))