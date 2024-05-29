import unittest
from calc import Calculations

class TestCalc(unittest.TestCase):

    def test_sum(self):
        calc_1: Calculations = Calculations(a=2, b=3)
        result: float = calc_1.get_sum()
        self.assertEqual(result, 5, msg=f"Error Test Failed, expected value 5, got {result}")

    def test_difference(self):
        calc_1: Calculations = Calculations(a=2, b=3)
        result: float = calc_1.get_difference()
        self.assertEqual(result, -1, msg=f"Error Test Failed")

    def test_product(self):
        calc_1: Calculations = Calculations(a=2, b=3)
        result: float = calc_1.get_product()
        self.assertEqual(result, 6, msg=f"Error Test Failed")

    def test_quotient(self):
        calc_1: Calculations = Calculations(a=2,b=3)
        result: float = calc_1.get_quotient()
        self.assertEqual(result, 2/3, msg="Error Test Failed")

if __name__ == "__main__":

    unittest.main()