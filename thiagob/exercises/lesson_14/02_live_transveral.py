class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None


# Pré-Orderm Esquerda, Raiz, Direita
def preorder(node):
    if node.left:
        preorder(node.left)
    print(node.value)
    if node.right:
        preorder(node.right)

# Em Ordem (Raiz, Esquerda, Direita)
def inorder(node):
    print(node.value)
    if node.left:
        inorder(node.left)
    if node.right:
        inorder(node.right)

# Pós-Ordem (Esquerda, Direita, Raiz)
def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.value)

n1 = Node('1')
n2 = Node('2')
n3 = Node('3')
n4 = Node('4')
n5 = Node('5')

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

print('preorder')
preorder(n1)

print('inorder')
inorder(n1)

print('postorder')
postorder(n1)