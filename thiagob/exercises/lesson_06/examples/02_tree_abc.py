class Node:
    # construtor desta minha classe
    def __init__(self, name):
        # conteúdo do nó
        if name != "":
            self.name = name
        else:
            self.name = "Sem nome"
        # arestas / ligação com os filhos
        self.children = []


class Carro:
    def __init__(self):
        print("Novo carro foi criado")


c1 = Carro()
c2 = Carro()

#sn = Node("")
#print(sn.name)

raiz = Node("A")
#print(raiz.name)
#print(raiz.children)

b = Node("B")
raiz.children.append(b)
#print(b.name)
#print(raiz.children)

c = Node("C")
raiz.children.append(c)
#print(c.name)

d = Node("D")
raiz.children.append(d)

e = Node("E")
b.children.append(e)

f = Node("F")
b.children.append(f)

k = Node("K")
e.children.append(k)

def print_node(node, level):
    print(".." * level + node.name)
    for child in node.children:
        print_node(child, level + 1)


print_node(raiz, 0)