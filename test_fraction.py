import unittest
import fraction

class TestFraction(unittest.TestCase):

    def setUp(self):
        self.half = fraction.Fraction(1,2)
        self.third = fraction.Fraction(1,3)
        self.quarter = fraction.Fraction(1,4)
        self.result = None
    
    def tearDown(self):
        del(self.half)
        del(self.third)
        del(self.quarter)
        del(self.result)
        
    def test_define(self):
        self.assertEqual(self.half, fraction.Fraction(1,2)) #shouldn't be possible to fail, but I'm nothing if not thurough
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
        self.assertEqual(self.half * self.half, self.quarter)
        self.assertEqual(self.third, self.third * fraction.Fraction(5,5))
        
    def test_truediv(self):
        self.assertEqual(self.half, self.quarter / self.half)
        with self.assertRaises(ZeroDivisionError):
            self.result = self.quarter / fraction.Fraction(0,5)
            
    def test_getter(self):
        self.assertEqual(self.half.num, 1)
        self.assertEqual(self.half.den, 2)
        
        
    def test_setter(self):
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

    
if __name__ == '__main__':
    unittest.main()