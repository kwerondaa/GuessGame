import unittest
from pirates import Ship

class TestShip(unittest.TestCase):
    def test_is_worthy(self):

        Titanic = Ship(15, 10)
        Noah = Ship(30, 10)

        self.assertEqual(Titanic.Is_worth_it(), False)
        self.assertEqual(Noah.Is_worth_it(), True)



