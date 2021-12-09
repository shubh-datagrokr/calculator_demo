import unittest
import calc


class TestCalculator(unittest.TestCase):

    def add_test(self):
        self.assertEqual(calc.add(1, 5), 6)
        self.assertIsNone(calc.add(12, ),)
    def sub_test(self):
        self.assertEqual(calc.subtract(5, 1), 4)
    def mul_test(self):
        self.assertEqual(calc.multiply(2, 6), 12)
    def divide_test(self):
        self.assertEqual(calc.divide(12, 4), 3)
        self.assertEqual(calc.divide(12, 0), "Can not divide a number by 0.")
        
    
