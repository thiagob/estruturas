from app import lib

stack = lib.lists.Stack()


class Roulette:

    def __init__(self):
        self.numbers = [0, 32 ,15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, \
            36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, \
            14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
        self.current = 0

    def move(self, positions):
        self.current += positions
        index = self.current % len(self.numbers)
        return self.numbers[index]


r = Roulette()
print(r.move(65437))
print(r.move(32486))
print(r.move(13486))
