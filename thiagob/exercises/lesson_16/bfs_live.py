class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


t = Node("T")
h = Node("h")
i = Node("i")
a = Node("a")
g = Node("g")
o = Node("o")

t.left = h
t.right = i

h.left = a
h.right = g

i.left = o


def bfs(node):
    # Primeiro adiciona-se o nó raiz na fila
    # Enquanto houver elementos na fila
        # Processa-se o primeiro elemento da fila
        # Adiciona-se os filhos na árvore