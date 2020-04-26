import unittest
from config import lib as lib

class StackTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_with_strings(self):
        stack = lib.Stack()
        stack.push("Azul")
        stack.push("Amarelo")

        stack.push("Vermelho")
        self.assertEqual(stack.pop(), "Vermelho")

        self.assertEqual(stack.top(), "Amarelo")
        self.assertEqual(stack.pop(),"Amarelo")
        self.assertEqual(stack.top(), "Azul")

        stack.push("Roxo")
        self.assertEqual(stack.pop(), "Roxo")

        self.assertEqual(stack.pop(), "Azul")
        assert stack.pop() == None

    def test_with_integers(self):
        stack = lib.Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)

        stack.push(5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), None)

