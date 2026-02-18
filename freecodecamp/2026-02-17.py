import unittest

# 2026 Winter Games Day 12: Bobsled
# Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.
#
# The length of the array determines the team size: 1, 2 or 4 person teams.
# All given weight values are in kilograms (kg).
# The bobsled (sled by iteself) must have a minimum weight of:
#
# 162 kg for a 1-person team
# 170 kg for a 2-person team
# 210 kg for a 4-person team
# The total weight of the bobsled (athletes plus sled) must not exceed:
#
# 247 kg for a 1-person team
# 390 kg for a 2-person team
# 630 kg for a 4-person team
# Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements.
#

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

bobsled_weight = {1: 162, 2: 170, 4: 210}
bobsled_total_team_weight = {1: 247, 2: 390, 4: 630}


def check_eligibility(athlete_weights, sled_weight):
    logging.debug(f"start of check_eligibility {(athlete_weights, sled_weight)=}")
    team_size = len(athlete_weights)
    total_weight = sum(athlete_weights) + sled_weight
    logging.debug(f"{(team_size,total_weight)}")
    if (
        sled_weight >= bobsled_weight[team_size]
        and total_weight <= bobsled_total_team_weight[team_size]
    ):
        return "Eligible"
    else:
        return "Not Eligible"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(check_eligibility([78], 165), "Eligible")
        self.assertEqual(check_eligibility([80], 160), "Not Eligible")
        self.assertEqual(check_eligibility([80], 170), "Not Eligible")
        self.assertEqual(check_eligibility([85, 90], 170), "Eligible")
        self.assertEqual(check_eligibility([85, 95], 168), "Not Eligible")
        self.assertEqual(check_eligibility([112, 97], 185), "Not Eligible")
        self.assertEqual(check_eligibility([110, 102, 90, 106], 222), "Eligible")
        self.assertEqual(check_eligibility([106, 99, 90, 88], 205), "Not Eligible")
        self.assertEqual(check_eligibility([106, 99, 103, 96], 227), "Not Eligible")


if __name__ == "__main__":

    unittest.main(verbosity=2)
