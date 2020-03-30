class Node:

    def __init__(self, text):
        self.previous = None
        self.next = None
        self.text = text

first = Node("Professor")
middle = Node("Thiago")
last = Node("Bohn")

first.next = middle
middle.next = last

last.previous = middle
middle.previous = first

print("Midle: %s | Previous: %s | Next: %s" % \
     (middle.text, middle.previous.text, middle.next.text))
# Node: Thiago | Previous: Professor | Next: Bohn