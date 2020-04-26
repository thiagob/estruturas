# https://i.pinimg.com/originals/9e/12/6f/9e126f728eb286d27a5cc8ff35a990e7.png

class Node:

    def __init__(self, name):
        # conteúdo do nó
        self.name = name
        # arestas / ligação com os filhos
        self.children = []

    def add_child(self, node):
        self.children.append(node)


root = Node("Shopping List")

drinks = Node("Drinks")
fruit = Node("Fruit")

root.add_child(drinks)
root.add_child(fruit)

# Drinks
water = Node("Water")
wine = Node("Wine")

drinks.add_child(water)
drinks.add_child(wine)

wine.add_child(Node("Red"))
wine.add_child(Node("White"))
wine.add_child(Node("Rose"))

# Fruits
fruits = ["Apples", "Pears", "Bananas", "Lemon"]
for f in fruits:
    fruit.add_child(Node(f))



print(root)