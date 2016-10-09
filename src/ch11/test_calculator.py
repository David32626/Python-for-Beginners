import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        self.calc = None
        self.answer = None

    def test_plus(self):
        self.answer = self.calc.plus(1, 2)
        self.assertEqual(self.answer, 3)

    def test_minus(self):
        self.answer = self.calc.minus(3, 1)
        self.assertEqual(self.answer, 2)

    def test_multiplied(self):
        self.answer = self.calc.multiplied(2, 4)
        self.assertEqual(self.answer, 7)

    def test_divided(self):
        self.answer = self.calc.divided(4, 2)
        self.assertEqual(self.answer, 2)

if __name__ == '__main__':
    unittest.main()