import random
import string

class PlateGenerator:

    def random_letter(self):
        letters = string.ascii_uppercase
        return random.choice(letters)

    def random_number(self):
        return random.randint(0, 9)

    def new_plate(self):
        plate = ""
        for i in range(8):
            if i in [0,1,2,4]:
                plate = plate + self.random_letter()
            else:
                plate = plate + str(self.random_number())
        return plate

class Veiculo:

    def __init__(self):
        self.placa = PlateGenerator().new_plate()

class Pickup(Veiculo):

    def __init__(self, capacidade_carga):
        super().__init__()
        self.capacidade_carga = capacidade_carga

    def carregar(self, carga):
        if carga > self.capacidade_carga:
            print("Erro: capacidade de carga excedida")
            return False
        else:
            return True

v = Veiculo()
print(v.placa)

p = Pickup(1000)
print(p.placa)
p.carregar(2000)