import statistics
import math

def inorder(root, a):
    if not root:
        return
    inorder(root.left, a)
    a.append(root.data)
    inorder(root.right, a)
    

def findMedian(root):
    a = []
    inorder(root, a)
    b = statistics.median(a)
    if (b - math.floor(b)) == 0:
        return int(b)
    return b