import unittest
import fraction

class TestFraction(unittest.TestCase):

    def setUp(self):
        """
        defining some fractions to play with
        """
        self.half = fraction.Fraction(1,2)
        self.third = fraction.Fraction(1,3)
        self.quarter = fraction.Fraction(1,4)
        self.result = None
    
    def tearDown(self):
        """
        cleaning up example fractions
        """
        del(self.half)
        del(self.third)
        del(self.quarter)
        del(self.result)
        
    def test_define(self):
        """
        tests the initialization process and its ability to filter out strings and floats
        """
        self.assertEqual(self.half, fraction.Fraction(1,2))
        with self.assertRaises(ValueError):
            fraction.Fraction("ham",2)
        with self.assertRaises(ValueError):
            fraction.Fraction(3,"sandwich")
        with self.assertRaises(ValueError):
            fraction.Fraction(1.5,3)
        with self.assertRaises(ValueError):
            fraction.Fraction(3,4.5)
                
    def test_str(self):
        self.assertEqual(str(self.half), "1/2")
        
    def test_add(self):
        self.result = self.quarter + self.third
        self.assertEqual(self.result, fraction.Fraction(7,12))
        
    def test_sub(self):
        self.assertEqual(self.half - self.quarter, self.quarter)
        self.assertEqual(self.quarter - self.half, fraction.Fraction(-1,4))
        
    def test_mul(self):
        """
        Checking ability to multiply and simplify
        """
        self.assertEqual(self.half * self.half, self.quarter)
        self.assertEqual(self.third, self.third * fraction.Fraction(5,5))
        
    def test_truediv(self):
        """
        testing ability to divide and toss div by 0
        """
        self.assertEqual(self.half, self.quarter / self.half)
        with self.assertRaises(ZeroDivisionError):
            self.result = self.quarter / fraction.Fraction(0,5)
            
    def test_getter(self):
        """
        testing @property getters self.num and self.den
        """
        self.assertEqual(self.half.num, 1)
        self.assertEqual(self.half.den, 2)
        
        
    def test_setter(self):
        """
        testing @property setters self.num and self.den
        """
        self.result = self.half
        self.result.num = 2
        self.result.den = 3
        self.assertEqual(self.result, fraction.Fraction(2,3))
        with self.assertRaises(ValueError):
            fraction.Fraction("ham",2)
        with self.assertRaises(ValueError):
            fraction.Fraction(3,"sandwich")
        with self.assertRaises(ValueError):
            fraction.Fraction(1.5,3)
        with self.assertRaises(ValueError):
            fraction.Fraction(3,4.5)

    def test_gt(self):
        self.assertTrue(self.half > self.third)
        
    def test_lt(self):
        self.assertTrue(self.third < self.half)

    def test_ge(self):
        self.assertTrue(self.half > self.third)
        self.assertTrue(self.half == self.half)

    def test_le(self):
        self.assertTrue(self.third < self.half)
        self.assertTrue(self.half == self.half)
        
if __name__ == '__main__':
    unittest.main()
