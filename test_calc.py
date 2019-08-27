import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

        #testing exceptions: method1
        self.assertRaises(ValueError, calc.divide, 10, 0)

        #testing exceptions: method2 (context manager)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)



if __name__ == '__main__':
    unittest.main()