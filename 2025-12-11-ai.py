import unittest


def to_roman(num):
    """Convert a number (1-3999) to Roman numerals."""
    if not 1 <= num <= 3999:
        raise ValueError("Number must be between 1 and 3999")
    
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ''
    for value, numeral in values:
        count = num // value
        if count:
            result += numeral * count
            num -= value * count
    
    return result


class TestRomanNumeralConverter(unittest.TestCase):
##    
##    def test_single_digits(self):
##        """Test conversion of single digit numbers"""
##        self.assertEqual(to_roman(1), 'I')
##        self.assertEqual(to_roman(2), 'II')
##        self.assertEqual(to_roman(3), 'III')
##        self.assertEqual(to_roman(4), 'IV')
##        self.assertEqual(to_roman(5), 'V')
##        self.assertEqual(to_roman(6), 'VI')
##        self.assertEqual(to_roman(7), 'VII')
##        self.assertEqual(to_roman(8), 'VIII')
##        self.assertEqual(to_roman(9), 'IX')
##    
##    def test_tens(self):
##        """Test conversion of multiples of 10"""
##        self.assertEqual(to_roman(10), 'X')
##        self.assertEqual(to_roman(20), 'XX')
##        self.assertEqual(to_roman(30), 'XXX')
##        self.assertEqual(to_roman(40), 'XL')
##        self.assertEqual(to_roman(50), 'L')
##        self.assertEqual(to_roman(60), 'LX')
##        self.assertEqual(to_roman(70), 'LXX')
##        self.assertEqual(to_roman(80), 'LXXX')
##        self.assertEqual(to_roman(90), 'XC')
##    
##    def test_hundreds(self):
##        """Test conversion of multiples of 100"""
##        self.assertEqual(to_roman(100), 'C')
##        self.assertEqual(to_roman(200), 'CC')
##        self.assertEqual(to_roman(300), 'CCC')
##        self.assertEqual(to_roman(400), 'CD')
##        self.assertEqual(to_roman(500), 'D')
##        self.assertEqual(to_roman(600), 'DC')
##        self.assertEqual(to_roman(700), 'DCC')
##        self.assertEqual(to_roman(800), 'DCCC')
##        self.assertEqual(to_roman(900), 'CM')
##    
##    def test_thousands(self):
##        """Test conversion of multiples of 1000"""
##        self.assertEqual(to_roman(1000), 'M')
##        self.assertEqual(to_roman(2000), 'MM')
##        self.assertEqual(to_roman(3000), 'MMM')
##    
##    def test_complex_numbers(self):
##        """Test conversion of complex numbers"""
##        self.assertEqual(to_roman(58), 'LVIII')
##        self.assertEqual(to_roman(1994), 'MCMXCIV')
##        self.assertEqual(to_roman(2024), 'MMXXIV')
##        self.assertEqual(to_roman(444), 'CDXLIV')
##        self.assertEqual(to_roman(888), 'DCCCLXXXVIII')
##        self.assertEqual(to_roman(1666), 'MDCLXVI')
##    
##    def test_edge_cases(self):
##        """Test edge cases at boundaries"""
##        self.assertEqual(to_roman(1), 'I')  # Minimum
##        self.assertEqual(to_roman(3999), 'MMMCMXCIX')  # Maximum
##        self.assertEqual(to_roman(49), 'XLIX')
##        self.assertEqual(to_roman(99), 'XCIX')
##        self.assertEqual(to_roman(999), 'CMXCIX')
##    
##    def test_historical_dates(self):
##        """Test conversion of common historical years"""
##        self.assertEqual(to_roman(1776), 'MDCCLXXVI')
##        self.assertEqual(to_roman(1945), 'MCMXLV')
##        self.assertEqual(to_roman(2000), 'MM')
##    
##    def test_invalid_input_below_range(self):
##        """Test that numbers below 1 raise ValueError"""
##        with self.assertRaises(ValueError):
##            to_roman(0)
##        with self.assertRaises(ValueError):
##            to_roman(-1)
##        with self.assertRaises(ValueError):
##            to_roman(-100)
##    
##    def test_invalid_input_above_range(self):
##        """Test that numbers above 3999 raise ValueError"""
##        with self.assertRaises(ValueError):
##            to_roman(4000)
##        with self.assertRaises(ValueError):
##            to_roman(5000)
##        with self.assertRaises(ValueError):
##            to_roman(10000)
##    
    def test_daily_coding_challenge(self): 
        self.assertEqual(to_roman(18), 'XVIII')
        self.assertEqual(to_roman(19), 'XIX')
        self.assertEqual(to_roman(1464), 'MCDLXIV')
        self.assertEqual(to_roman(2025), 'MMXXV')
        self.assertEqual(to_roman(3999), 'MMMCMXCIX')

if __name__ == '__main__':
    unittest.main(verbosity=2)