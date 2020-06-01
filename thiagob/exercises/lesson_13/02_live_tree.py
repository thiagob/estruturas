class Node:

    def __init__(self, data, root=False):
        self.data = data
        self.childs = []
        self.root = root

    def add_child(self, node):
        self.childs.append(node)

    def is_root_node(self):
        return self.root

    def is_leaf_node(self):
        return len(self.childs) == 0    

    def is_internal_node(self):
        return len(self.childs) > 0    

    
    def calculate_level(self, current_level=0):
        self.level = current_level
        for child in self.childs:
            child.calculate_level(self.level + 1)

    def print_tree(self):
        attributes = []

        if self.is_root_node():
            attributes.append("Root")
        if self.is_leaf_node():
            attributes.append("Leaf")
        if self.is_internal_node():
            attributes.append("Internal")

        print((".." * self.level) + self.data + " (" + ", ".join(attributes) + " | Level: " + str(self.level) + ")")
        
        for child in self.childs:
            child.print_tree()

root = Node("Brasil", root=True)

r_sul = Node("Região Sul")
r_sul.add_child(Node("Rio Grande do Sul"))
r_sul.add_child(Node("Santa Catarina"))

r_sudeste = Node("Região Sudeste")
r_sudeste.add_child(Node("Rio de Janeiro"))
r_sudeste.add_child(Node("São Paulo"))

r_central = Node("Região Central")
r_central.add_child(Node("Distrito Federal"))
r_central.add_child(Node("Mato Grosso"))

root.add_child(r_sul)
root.add_child(r_sudeste)
root.add_child(r_central)

root.calculate_level()
root.print_tree()


#print(br.level)
#print(r_sul.level)
