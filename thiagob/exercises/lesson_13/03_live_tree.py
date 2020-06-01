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

        print((".." * self.level) + self.data["name"] + ">>>" + str(self.data["sales"]) + "<<<" + " (" + ", ".join(attributes) + " | Level: " + str(self.level) + ")")
        
        for child in self.childs:
            child.print_tree()

root = Node({"name": "Brasil", "sales": 100}, root=True)
root.calculate_level()
root.print_tree()
