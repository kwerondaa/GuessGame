

import unittest
import guessgame

class TestGuess(unittest.TestCase):
    def test_if_guess_true(self):
        self.assertEqual(guessgame.guessGame(), True)
        self.assertEqual(guessgame.guessGame(), False )

if __name__ == "__main__":
    unittest.main()

















