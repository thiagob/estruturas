class Node:

    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:

    def __init__(self):
        # head, or could be even node
        self.first = None
        self.last = None


    def append(self, value):
        new_node = Node(value)

        # list is emtpy
        if self.first is None:
            self.first = new_node
        # has other nodes
        else:
            self.last.next = new_node

        self.last = new_node


    def print(self):
        node = self.first

        i = 0
        while (node):
            print('[%i] %s ' % (i, str(node.value)))
            node = node.next
            i += 1


    def insert(self, index, value):
        new_node = Node(value)

        if index == 0:
            new_node.next = self.first
            self.first = new_node
        else:           
            i = 1
            node = self.first
            while (i <= index):
                if node is None:
                    raise Exception("Index %i is out of the range." % (index))

                if i == index:
                    new_node.next = node.next
                    node.next = new_node
                    return

                node = node.next
                i += 1


    def delete(self, index):
        if self.first:
            if index == 0:
                self.first = self.first.next
            else:
                i = 0
                node = self.first
                while (i <= index):
                    if node is None or node.next is None:
                        raise Exception("Index %i is out of the range." % (index))

                    if i == (index - 1):
                        node.next = node.next.next
                        return

                    node = node.next
                    i += 1

    def sort(self):
        # check if the list has at least 2 elements
        if self.first and self.first.next:
            while(True):
                swapped = False

                if self.first.value > self.first.next.value:
                    minor = self.first.next
                    self.first.next = minor.next
                    minor.next = self.first
                    self.first = minor
                    swapped = True

                previous = self.first
                node = previous.next

                while node and node.next:
                    if node.value > node.next.value:
                        minor = node.next

                        node.next = minor.next
                        previous.next = minor
                        minor.next = node

                        swapped = True

                    previous = node
                    node = node.next

                if not swapped:
                    break

        def find(self, value):
            pass
    
        def length(self):
            pass

str_list = LinkedList()
str_list.append("Azul")
str_list.append("Preto")
str_list.append("Rosa")
str_list.print()

print('====')

str_list.insert(0, "Branco")
str_list.print()

print('====')

str_list.insert(1, "Vermelho")
str_list.print()


print('====')

str_list.delete(1)
str_list.print()

print('====')

int_list = LinkedList()
int_list.append(5)
int_list.append(3)
int_list.append(99)
int_list.append(13)
int_list.append(7)
int_list.append(25)
int_list.sort()
int_list.print()