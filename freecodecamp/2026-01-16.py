import unittest

# Integer Hypotenuse
# Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.
# 
# The length of the hypotenuse is calculated by adding the squares of the two leg lengths together and then taking the square root of that total (a2 + b2 = c2).

import logging
import math
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def is_integer_hypotenuse(a,b):
    logging.debug('start of is_integer_hypotenuse')
    c= math.sqrt(a**2+b**2)
    return c == int(c)

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(is_integer_hypotenuse(3, 4) , True)
        self.assertEqual(is_integer_hypotenuse(2, 3) , False)
        self.assertEqual(is_integer_hypotenuse(5, 12) , True)
        self.assertEqual(is_integer_hypotenuse(10, 10) , False)
        self.assertEqual(is_integer_hypotenuse(780, 1040) , True)
        self.assertEqual(is_integer_hypotenuse(250, 333) , False)

if __name__ == '__main__':

    unittest.main(verbosity=2)


