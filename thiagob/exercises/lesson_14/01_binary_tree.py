class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None


def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.value)
    if node.right:
        inorder(node.right)

def preorder(node):
    pass

def postorder(node):
    pass

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')

a.left = b
a.right = c

b.left = d
d.left = g

c.left = e
c.right = f

e.left = h
e.right = i

inorder(a)