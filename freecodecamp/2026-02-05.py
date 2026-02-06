import unittest

# Pocket Change
# Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".
#
# 100 cents equals 1 dollar.
# In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def count_change(args):
    logging.debug(f"start of count_change {args=}")
    cents = sum(args)
    ret = f"${cents/100:.2f}" 
    print(ret)
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(count_change([25, 10, 5, 1]), "$0.41")
        self.assertEqual(
            count_change([25, 10, 5, 1, 25, 10, 25, 1, 1, 10, 5, 25]), "$1.43"
        )
        self.assertEqual(count_change([100, 25, 100, 1000, 5, 500, 2000, 25]), "$37.55")
        self.assertEqual(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]), "$0.70")
        self.assertEqual(count_change([1]), "$0.01")
        self.assertEqual(count_change([25, 25, 25, 25]), "$1.00")


if __name__ == "__main__":

    unittest.main(verbosity=2)
