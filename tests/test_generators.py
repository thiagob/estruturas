import unittest
from config import lib as lib

class GeneratorsTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_small_list_of_ints(self):
        lst = lib.generate_list_of_ints(3, 20)
        assert len(lst) == 3
        for i in lst:
            assert i <= 20
