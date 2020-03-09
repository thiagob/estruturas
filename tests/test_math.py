import unittest
from config import lib as lib

class MathTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_recursive_fibonacci(self):
        assert lib.fibonacci_r(0) == 0     
        assert lib.fibonacci_r(1) == 1
        assert lib.fibonacci_r(2) == 1
        assert lib.fibonacci_r(3) == 2
        assert lib.fibonacci_r(4) == 3
        assert lib.fibonacci_r(5) == 5
        assert lib.fibonacci_r(14) == 377

    def test_iterative_fibonacci(self):
        assert lib.fibonacci_i(0) == 0     
        assert lib.fibonacci_i(1) == 1
        assert lib.fibonacci_i(2) == 1
        assert lib.fibonacci_i(3) == 2
        assert lib.fibonacci_i(4) == 3
        assert lib.fibonacci_i(5) == 5
        assert lib.fibonacci_i(14) == 377

if __name__ == '__main__':
    unittest.main()