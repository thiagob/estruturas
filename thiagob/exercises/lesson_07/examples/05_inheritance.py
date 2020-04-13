class Animal:
    patas = 4

class Cachorro(Animal):

    def latir(self):
        print("Au au")

class Galinha(Animal):

    def __init__(self):
        self.patas = 2

    def cacarejar(self):
        print("Có có có")

c = Cachorro()
c.latir()
print(c.patas)

g = Galinha()
g.cacarejar()
print(g.patas)

a = Animal()
print(a.patas)
#a.latir()