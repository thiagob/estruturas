class Node:

    def __init__(self, data, level=0, root=False):
        self.data = data
        self.level = level
        self.root = root
        self.childs = []


    def add_child(self, node):
        self.childs.append(node)

    def is_root_node(self):
        return self.root

    def is_leaf_node(self):
        return len(self.childs) == 0    

    def is_internal_node(self):
        return len(self.childs) > 0    

    def get_total_sales(self):
        total = 0
        for child in self.childs:
            total = total + child.get_total_sales()

        if "sales" in self.data:
            return self.data["sales"] + total
        else:
            return total


    def print_tree(self):
        attributes = []

        if self.is_root_node():
            attributes.append("Root")
        if self.is_leaf_node():
            attributes.append("Leaf")
        if self.is_internal_node():
            attributes.append("Internal")

        print(".." * self.level + self.data["name"] + " Sales: " + '{:6,.2f}'.format(self.get_total_sales()) + ")")
        
        for child in self.childs:
            child.print_tree()

    def calculate_level(self, current_level=0):
        self.level = current_level
        for child in self.childs:
            child.calculate_level(self.level + 1)


root = Node({
    "name": "Brasil"
}, root=True)

r_sul = Node({
    "name": "Região Sul"
})
r_sul.add_child(Node({
    "name": "Rio Grande do Sul",
    "sales": 110000
}))
r_sul.add_child(Node({
    "name": "Santa Catarina",
    "sales": 110000
}))


r_sudeste = Node({
    "name": "Região Sudeste"
})
r_sudeste.add_child(Node({
    "name": "Rio de Janeiro",
    "sales": 110000
}))
r_sudeste.add_child(Node({
    "name": "São Paulo",
    "sales": 120000
}))

r_central = Node({
    "name": "Região Central"
})
r_central.add_child(Node({
    "name": "Distrito Federal",
    "sales": 54000
}))
r_central.add_child(Node({
    "name": "Mato Grosso",
    "sales": 35000
}))

root.add_child(r_sul)
root.add_child(r_sudeste)
root.add_child(r_central)

root.calculate_level()
root.print_tree()