

import unittest
import guessgame

class TestGuess(unittest.TestCase):
    def test_if_guess_true(self):
        self.assertEqual(guessgame.guessGame(), True) #since i didn't add any arguments in the function back in the program file, how do I test it now?
        self.assertEqual(guessgame.guessGame(), False )

if __name__ == "__main__":
    unittest.main()

















