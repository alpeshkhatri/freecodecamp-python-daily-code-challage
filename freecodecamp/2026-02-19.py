import unittest

# 2026 Winter Games Day 14: Ski Mountaineering
# Given the snow depth and slope of a mountain, determine if there's an avalanche risk.

# The snow depth values are "Shallow", "Moderate", or "Deep".
# Slope values are "Gentle", "Steep", or "Very Steep".
# Return "Safe" or "Risky" based on this table:

# "Shallow"	"Moderate"	"Deep"
# "Gentle"	"Safe"	"Safe"	"Safe"
# "Steep"	"Safe"	"Risky"	"Risky"
# "Very Steep"	"Safe"	"Risky"	"Risky"


import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def avalanche_risk(snow_depth, slope):
    logging.debug(f"start of avalanche_risk {(snow_depth, slope)=}")
    if snow_depth == "Shallow":
        return "Safe"
    else:
        if slope == "Gentle":
            return "Safe"
    return "Risky"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(avalanche_risk("Shallow", "Gentle"), "Safe")
        self.assertEqual(avalanche_risk("Shallow", "Steep"), "Safe")
        self.assertEqual(avalanche_risk("Shallow", "Very Steep"), "Safe")
        self.assertEqual(avalanche_risk("Moderate", "Gentle"), "Safe")
        self.assertEqual(avalanche_risk("Moderate", "Steep"), "Risky")
        self.assertEqual(avalanche_risk("Moderate", "Very Steep"), "Risky")
        self.assertEqual(avalanche_risk("Deep", "Gentle"), "Safe")
        self.assertEqual(avalanche_risk("Deep", "Steep"), "Risky")
        self.assertEqual(avalanche_risk("Deep", "Very Steep"), "Risky")


if __name__ == "__main__":

    unittest.main(verbosity=2)
