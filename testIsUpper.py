import unittest
import isUpperCase

class TestIsUpper(unittest.TestCase):



    def test_ifString_isUpper(self):

        self.assertEqual(isUpperCase.is_uppercase("c"), False)
        self.assertEqual(isUpperCase.is_uppercase("C"), True)
        self.assertEqual(isUpperCase.is_uppercase("hello I AM DONALD"), False)
        self.assertEqual(isUpperCase.is_uppercase("HELLO I AM DONALD"), True)
        self.assertEqual(isUpperCase.is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ"), False)
        self.assertEqual(isUpperCase.is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"), True)

        self.assertEqual(isUpperCase.is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ"), True)








if __name__ == "__main__":
    unittest.main()

