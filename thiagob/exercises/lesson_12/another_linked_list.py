class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



class AnotherLinkedList:

    def __init__(self):

        self.next = None
        self.last = None

    def first(self):
        return self.next

    def append(self, value):
        new_node = Node(value)

        node = self
        while (node.next):
            node = node.next

        node.next = new_node


    def print(self):
        i = 0
        node = self.next
        i = 0
        while (node):
            print('[%i] %s ' % (i, str(node.value)))
            node = node.next
            i += 1


str_list = AnotherLinkedList()
str_list.append("Azul")
str_list.append("Preto")
str_list.append("Rosa")
str_list.print()

print('====')