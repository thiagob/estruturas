class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.first = None

    def append(self, value):
        n = Node(value)

        if self.first is None:
            self.first = n
        else:
            node = self.first

            while (node.next):
                node = node.next

            node.next = n


    def print(self):
        node = self.first

        i = 0
        while node:
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
int_list = LinkedList()
int_list.append(4)
int_list.append(5)
int_list.append(6)
int_list.print()

print('-------------')

# Before: 4, 5, 6
int_list.insert(1, 0)
# After: 4, 0, 5, 6
int_list.print()

print('-------------')

# Before: 4, 0, 5, 6
int_list.delete(0)
# After: 0, 5, 6

int_list.print()


print('-------------')

# Before: 0, 5, 6
int_list.delete(2)
# After: 0, 5

int_list.print()