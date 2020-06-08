class Node:

    def __init__(self, value):
        self.value = value
        self.childs = [None, None]


    @property
    def left(self):
        return self.childs[0]

    @left.setter
    def left(self, value):
        if value != self:
            self.childs[0] = value


a = Node('a')
b = Node('b')
c = Node('c')

# adicona B à esquerda
#a.childs[0] = b


# adicona B à esquerda
a.left = b
a.left = a
print(a.left.value)