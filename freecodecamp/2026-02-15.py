import unittest

# 2026 Winter Games Day 10: Alpine Skiing
# Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.
#
# To determine the rating:
#
# Calculate the steepness of the hill by taking the drop divided by the distance.
# Then, calculate the adjusted steepness based on the hill type:
# "Downhill" multiply steepness by 1.2
# "Slalom": multiply steepness by 0.9
# "Giant Slalom": multiply steepness by 1.0
# Return:
#
# "Green" if the adjusted steepness is less than or equal to 0.1
# "Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
# "Black" if the adjusted steepness is greater than 0.25

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

hill_type_adjustments = {"Downhill": 1.2, "Slalom": 0.9, "Giant Slalom": 1.0}


def get_hill_rating(drop, distance, hill_type):
    logging.debug(f"start of get_hill_rating {(drop, distance, hill_type)=}")
    steepness = drop / distance
    adjusted_steepness = steepness * hill_type_adjustments[hill_type]
    if 0 <= adjusted_steepness <= 0.1:
        return "Green"
    elif 0.1 < adjusted_steepness <= 0.25:
        return "Blue"
    else:
        return "Black"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_hill_rating(95, 900, "Slalom"), "Green")
        self.assertEqual(get_hill_rating(620, 2800, "Downhill"), "Black")
        self.assertEqual(get_hill_rating(420, 1680, "Giant Slalom"), "Blue")
        self.assertEqual(get_hill_rating(250, 3000, "Downhill"), "Green")
        self.assertEqual(get_hill_rating(110, 900, "Slalom"), "Blue")
        self.assertEqual(get_hill_rating(380, 1500, "Giant Slalom"), "Black")


if __name__ == "__main__":

    unittest.main(verbosity=2)
