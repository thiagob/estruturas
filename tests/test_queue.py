import unittest
from config import lib as lib

class QueueTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_with_strings(self):
        q = lib.Queue()
        q.enqueue("Primeiro")
        q.enqueue("Segundo")
        q.enqueue("Terceiro")

        self.assertEqual(q.dequeue(), "Primeiro")
        
        q.enqueue("Quarto")
        self.assertEqual(q.dequeue(), "Segundo")
        self.assertEqual(q.dequeue(), "Terceiro")
        self.assertEqual(q.dequeue(), "Quarto")
        assert q.is_empty()