import unittest
from config import lib as lib

class StackStringTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_with_list_of_strings(self):
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
