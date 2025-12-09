# test_main.py
import unittest
from main import addition

class TestMonProjet(unittest.TestCase):
    def test_addition(self):
        # On vérifie que 2 + 3 donne bien 5
        self.assertEqual(addition(2, 3), 5)
        # On vérifie que 10 + (-1) donne bien 9
        self.assertEqual(addition(10, -1), 9)

if __name__ == '__main__':
    unittest.main()