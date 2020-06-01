class Node:
    def __init__(self, value):
        self.value = value 
        self.childs = [None, None]

    @property
    def left(self):
        return self.childs[0]

    @left.setter
    def left(self, left):
        self.childs[0] = left

    @property
    def right(self):
        return self.childs[1]

    @right.setter
    def right(self, left):
        self.childs[1] = left


a = Node('a')
b = Node('b')
c = Node('c')

a.childs[0] = b
a.childs[1] = c

print(a.childs)
print(a.left.value)
print(a.right.value)
