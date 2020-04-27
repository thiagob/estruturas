class BaseList:

    def __init__(self, debug=False):
        self.elements = []
        self.debug = debug

    # imprive a pilha no seu estado atual
    def print(self, element=None):
        if self.debug:
            if element:
                print(str(element))
            print("[%s]" % ", ".join(map(str, self.elements)))

    # retorna o tamanho da pilha
    def length(self):
        return len(self.elements)


class Stack(BaseList):

    # acessa-se o elemento posicionado no topo da pilha
    def top(self):
        if self.length() > 0:
            return self.elements[0]
        else:
            return None

    # insere um novo elemento no topo da pilha
    def push(self, element):
        self.elements.insert(0, element)
        self.print()

    # remove o elemento do topo da pilha
    def pop(self):
        elem = None
        if self.length() > 0:
            elem = self.elements.pop(0)

        self.print(elem)
        return elem

class Queue(BaseList):

    # inserir um elemento no final da fila
    def enqueue(self, element):
        self.elements.append(element)
        self.print()

    # remover um elemento do começo da fila
    def dequeue(self):
        elem = None
        if self.length() > 0:
            elem = self.elements.pop(0)

        self.print(elem)
        return elem

    def is_empty(self):
        return self.length() == 0

if __name__ == "__main__":
    # execute only if run as a script
    s = Stack(True)
    s.push("Azul")
    s.push("Vermelho")
    s.push("Preto")
    s.pop()
    s.push("Roxo")

    q = Queue(True)
    q.enqueue("Primeiro")
    q.enqueue("Segundo")
    q.enqueue("Terceiro")
    q.dequeue()
    q.enqueue("Quarto")