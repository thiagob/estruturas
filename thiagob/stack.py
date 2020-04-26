class Stack:

    def __init__(self, debug=False):
        self.elements = []
        self.debug = debug

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
        if self.debug:
            self.print(elem)
        return elem

    # imprive a pilha no seu estado atual
    def print(self, element=None):
        if self.debug:
            if element:
                print(element)
            print("[%s]" % ", ".join(self.elements))

    # returna o tamanho da pilha
    def length(self):
        return len(self.elements)


if __name__ == "__main__":
    # execute only if run as a script
    s = Stack(True)
    s.push("Azul")
    s.push("Vermelho")
    s.push("Preto")
    s.pop()
    s.push("Roxo")