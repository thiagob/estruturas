class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, node):
        pass

    def search(self, value):
        pass


tree = BST()
tree.insert(Node(8))

tree.insert(Node(3))
tree.insert(Node(10))

tree.insert(Node(1))
tree.insert(Node(6))
tree.insert(Node(14))

tree.insert(Node(4))
tree.insert(Node(7))
tree.insert(Node(13))

print(tree)

n = tree.search(7)

if n:
    print(n.value)
else:
    print("Number not found!")