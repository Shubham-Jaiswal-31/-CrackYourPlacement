class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
head = None
def printLL():
    t = head
    while (t != None):
        print(t.data, end=" ->")
        t = t.next
    print()
 
def swap(a, b):
    if(a == None or b == None):
        return
    temp = a.data
    a.data = b.data
    b.data = temp

def zigZag(node, flag):
    if(node == None or node.next == None):
        return node
    if (flag == 0):
        if (node.data > node.next.data):
            swap(node, node.next)
        return zigZag(node.next, 1)
 
    else:
        if (node.data < node.next.data):
            swap(node, node.next)
        return zigZag(node.next, 0)
 
 
head = Node(11)
head.next = Node(15)
head.next.next = Node(20)
head.next.next.next = Node(5)
head.next.next.next.next = Node(10)
printLL()
flag = 0
zigZag(head, flag)
print("LL in zig zag fashion : ")
printLL()