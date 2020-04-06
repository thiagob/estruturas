class Node:
    def __init__(self, name):
        self.name = name
        self.children = []


root = Node("Estruturas Avançadas de Dados")

node = Node("Listas Lineares")

node.children.append(Node("Alocação Sequencial"))
node.children[0].children.append(Node("Array"))
node.children[0].children.append(Node("Pilha ou Stack"))
node.children[0].children.append(Node("Fila ou Queue"))

node.children.append(Node("Alocação Encadeada"))
node.children[1].children.append(Node("Lista Simplesmente Encadeada"))
node.children[1].children.append(Node("Pilha Encadeada"))
node.children[1].children.append(Node("Fila Encadeada"))
node.children[1].children.append(Node("Listas Duplamente Encadeadas"))
node.children[1].children.append(Node("Listas Circulares"))

root.children.append(node)

root.children.append(Node("Árvores"))

def print_node(node, level):
    print(".." * level + node.name)
    for child in node.children:
        print_node(child, level + 1)


print_node(root, 0)