'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def constructTree(pre, preLN, n):
    i = 0
    def dfs():
        nonlocal i
        if i >= n:
            return None
        node = Node(pre[i])
        if preLN[i] == 'N':
            i += 1
            node.left = dfs()
            i += 1
            node.right = dfs()
        return node

    return dfs()
