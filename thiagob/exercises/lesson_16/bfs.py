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
    queue = []
    # Primeiro adiciona-se o nó raiz na fila
    queue.append(node)

    # Enquanto houver elementos na fila
    while queue:
        # Processa-se o primeiro elemento da fila
        n = queue.pop(0)
        print(n.data)

        # Adiciona-se os filhos na árvore
        if n.left:
            queue.append(n.left)

        if n.right:
            queue.append(n.right)


q = []
bfs(t, q)