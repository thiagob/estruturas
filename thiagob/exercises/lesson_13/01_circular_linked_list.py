class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:

    def __init__(self):

        self.first = None
        self.last = None
        self.current = None

    def next(self):
        if self.first:
            # first time next is called
            if self.current is None:
                self.current = self.first
            else:
                self.current = self.current.next
            return self.current
        else:
            return None

    def append(self, value):
        n = Node(value)

        if self.first is None:
            self.first = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n

        self.last = n
        self.last.next = self.first

        return n

    def delete(self, node):
        previous = self.first
        while previous.next != node:
            previous = previous.next

        previous.next = node.next
        if self.first == node:
            self.first = node.next
        if self.current == node:
            self.current = node.next
        if self.last == node:
            self.last = previous

c_lst = CircularLinkedList()
dom = c_lst.append("Domingo")
seg = c_lst.append("Segunda")
ter = c_lst.append("Terça")
qua = c_lst.append("Quarta")
qui = c_lst.append("Quinta")
sex = c_lst.append("Sexta")
sab = c_lst.append("Sábado")

c_lst.delete(dom)
c_lst.delete(sab)

dom = c_lst.append("FERIADO")

while True:
    nxt = c_lst.next()
    print(nxt.value if nxt else None)
    if input("Print another one? (Y/N)").lower() == "n":
        break

