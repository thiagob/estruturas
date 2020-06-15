class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            parent = self.root
            
            while True:
                if node.value <= parent.value:
                    if parent.left is None:
                        parent.left = node
                        return
                    else:
                        parent = parent.left
                else:
                    if parent.right is None:
                        parent.right = node
                        return
                    else:
                        parent = parent.right

    def search(self, value):
        node = self.root
        while True:
            if value == node.value:
                return node
            elif value <= node.value and node.left:
                node = node.left
            elif value > node.value and node.right:
                node = node.right
            else:
                return None


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