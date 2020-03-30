class Node:

    def __init__(self, text, next):
        self.previous = None
        self.text = text
        self.next = next
        if next:
            self.next.previous = self 

n1 = Node("Bohn", None)
n2 = Node("Thiago", n1)
n3 = Node("Professor", n2)

print("Node: %s | Previous: %s | Next: %s" % (n2.text, n2.previous.text, n2.next.text))
# Node: Thiago | Previous: Professor | Next: Bohn