import unittest

# 2026 Winter Games Day 7: Speed Skating
# Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.
# 
# The first element of each array corresponds to lap 1, the second to lap 2, and so on.
 
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def largest_difference(skater1, skater2):
    logging.debug(f"start of largest_difference {skater1=} {skater2=}")
    largest_diff = 0 
    lap_number = 0
    largest_diff_lap_number = 0
    for s1,s2 in zip(skater1, skater2) :
        diff = abs(s1 - s2)
        lap_number = lap_number + 1
        if diff >= largest_diff :
            largest_diff = diff
            largest_diff_lap_number = lap_number
    return largest_diff_lap_number


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]) , 3)
        self.assertEqual(largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]) , 1)
        self.assertEqual(largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95]) , 5)
        self.assertEqual(largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01]) , 2)
        self.assertEqual(largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10]) , 4)



if __name__ == "__main__":

    unittest.main(verbosity=2)
