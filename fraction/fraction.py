def gcd(m, n):
    """A method to determine the greatest common denominator of m and n

    Parameters:
        m (int): an integer
        n (int): another integer
    Returns:
        n (int): the gcd of parameters m and n
    """
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    """
    This is a class for operations on fractions.

    This class is only valid for quotients of integers with positive integers, and does not support interactions with other classes.

    Attributes:
        _num(int): The numerator of the fraction.
        _den (int): The denominator of the fraction.
    """

    def __init__(self, top, bottom):
        if isinstance(top,int) and isinstance(bottom, int): #checking inputs
            self._num = top
            self._den = bottom
        else:
            raise ValueError("enter numerator, denominator as integer")
        """
        The constructor for Fraction class.

        Paramaters:
          top (int): The numerator of the fraction.
          bottom (int): The denominator of the fraction.
        """

    def __str__(self):
        """
        The string conversion method.

        Returns:
        str: A string representation of the fraction.
        """

        return str(self._num) + "/" + str(self._den)

    def show(self):
        """
        The show method for Fraction class

        Prints string conversion to console.
        """

        print(str(self))

    def __add__(self, otherfraction):
        """
        The method to add two Fractions.

        Parameters:
          otherfraction (Fraction): the fraction to be added.

        Returns:
          Fraction: A fraction containing the sum>
        """

        newnum = self._num * otherfraction._den + \
                 self._den * otherfraction._num
        newden = self._den * otherfraction._den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __sub__(self, otherfraction):
        """
        The method to subtract two Fractions.

        Parameters:
            otherfraction (Fraction): the fraction to be added.

        Returns:
            Fraction: A fraction containing the sum>
        """

        newnum = self._num * otherfraction._den - \
                 self._den * otherfraction._num
        newden = self._den * otherfraction._den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        """
        The method to mulitply two Fractions.

        Parameters:
          otherfraction (Fraction): the fraction to be multiplied.

        Returns:
          Fraction: A fraction containing the product>
        """

        newnum = self._num * otherfraction._num
        newden = self._den * otherfraction._den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __truediv__(self, otherfraction):
        """
        The method to divide one Fraction by another.

        Parameters:
          otherfraction (Fraction): the fractional divisor.

        Returns:
          Fraction: A fraction containing the quotient>
        """
        if otherfraction.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
        
            newnum = self._num * otherfraction._den
            newden = self._den * otherfraction._num
            common = gcd(newnum, newden)
            return Fraction(newnum // common, newden // common)

    def __eq__(self, otherfraction):
        """
        The method to check deep equality between two Fractions.

        Parameters:
          otherfraction (Fraction): the fraction to be multiplied.

          Returns:
            bool: a boolean asserting the equality of the two fractions.
          """

        firstnum = self._num * otherfraction._den
        secondnum = otherfraction._num * self._den

        return firstnum == secondnum

    def __ne__(self, otherfraction):

        return (not self == otherfraction)
            
    
    def __lt__(self, otherfraction):
        """
        The fractional less than method.

        Parameters:
          otherfraction(Fraction): Fraction supposed to be greater.

        Returns:
          bool: a boolean asserting first fraction is less than second.
        """

        firstnum = self._num * otherfraction._den
        secondnum = otherfraction._num * self._den

        return firstnum < secondnum

    def __gt__(self, other):
        """
        The fractional greater than method.

        Parameters:
          otherfraction(Fraction): Fraction supposed to be lesser.

        Returns:
          bool: a boolean asserting first fraction is greater than second.
        """

        return (not self < other) and (not self == other)

    def __le__(self, other): #fractional <= operator
        return (self < other or self == other)

    def __ge__(self, other): #fractional >= operator

        return (self > other or self == other)
    
    @property #numerator getter
    def num(self):
        return self._num
    @num.setter #numerator setter
    def num(self, val):
        if isinstance(val, int):  #checking if is int
            self._num = val
        else:
            raise ValueError()

    @property #denominator getter
    def den(self):
        return self._den
    @den.setter #deniminator setter
    def den(self, val):
        if isinstance(val,int) and val != 0:  #checking if is int
            if val < 0:
            
                self._den = abs(val)  #correcting to negative num over positive den
                self._num = -self._num
            else:
                self._den = val
        else:
            raise ValueError("enter numerator, denominator as integer arguments")
