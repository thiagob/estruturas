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

pg = PlateGenerator()
print(pg.new_plate())