class Node:

    def __init__(self, text, next):
        self.text = text
        self.next = next

n1 = Node("Bohn", None)
n2 = Node("Thiago", n1)
n3 = Node("Professor", n2)


n = n3
while (n != None):
    print(n.text)
    n = n.next


# Result >>
# Professor
# Thiago
# Bohn