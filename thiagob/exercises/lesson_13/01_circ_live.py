class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:

    def __init__(self):

        self.first = None
        self.last = None
        self.current = None


    def append(self, value):

        n = Node(value)
        
        # a lista é vazia
        if self.first is None:
            self.first = n
            self.first.next = self.first
        else:
            self.last.next = n
            n.next = self.first
        
        self.last = n

        return n

    def next(self):
        # primeira vez que chama o método
        if self.current is None:
            self.current = self.first
        else:
            self.current = self.current.next

        return self.current


    def delete(self, node):
        previous = node
        while previous.next != node:
            previous = previous.next

        previous.next = node.next

        if self.first == node:
            self.first = node.next
        
        # está faltando, quando quero deletar o elemento atual (current), o útlimo, ...


l = CircularLinkedList()
dom = l.append("Domingo")
l.append("Segunda")
l.append("Terça")
l.append("Quarta")
l.append("Quinta")
l.append("Sexta")
l.append("Sábado")

# print(l.first.value)
# print(l.first.next.value)
# print(l.first.next.next.value)

print("&&&&&&&&")
l.delete(dom)

for i in range(10):
    print(l.next().value)

