import unittest

# 2026 Winter Games Day 3: Biathlon
# Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.
#
# Each round consists of 5 targets.
# Each missed target results in a 150 meter penalty loop.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def calculate_penalty_distance(args):
    logging.debug(f"start of calculate_penalty_distance {args=}")
    ret = 0
    for i in args:
        ret = ret + (5 - i) * 150 
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(calculate_penalty_distance([4, 4]), 300)
        self.assertEqual(calculate_penalty_distance([5, 5]), 0)
        self.assertEqual(calculate_penalty_distance([4, 5, 3, 5]), 450)
        self.assertEqual(calculate_penalty_distance([5, 4, 5, 5]), 150)
        self.assertEqual(calculate_penalty_distance([4, 3, 0, 3]), 1500)


if __name__ == "__main__":

    unittest.main(verbosity=2)
