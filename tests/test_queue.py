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

    def test_with_integers(self):
        q = lib.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.dequeue(), 1)
        
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertEqual(q.dequeue(), 4)
        assert q.is_empty()