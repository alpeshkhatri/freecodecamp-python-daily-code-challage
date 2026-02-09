import unittest

# 2026 Winter Games Day 4: Ski Jumping
# Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.
#
# Your score is calculated by summing the above four values.
# The current total scores of the other jumpers are:
#
# 165.5
# 172.0
# 158.0
# 180.0
# 169.5
# 175.0
# 162.0
# 170.0
# If your score is the best, return "Gold"
# If it's second best, return "Silver"
# If it's third best, return "Bronze"
# Otherwise, return "No Medal"

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def skiJumpMedal(distance_points, style_points, wind_comp, k_point_bonus):
    total_score = sum([distance_points, style_points, wind_comp, k_point_bonus])
    others_scores = sorted([165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0], reverse=True)
    medals = ["Gold", "Silver", "Bronze", "No Medal" ]
    for idx,o in enumerate(others_scores[:3]) :
        logging.debug(f"start of skiJumpMedal {total_score=} {others_scores=} {idx=} {o=}")
        if total_score > o and idx == 0 :
            return "Gold"
        elif total_score > o and idx == 1 :
            return "Silver"
        elif total_score > o and idx == 2 :
            return "Bronze"
    return "No Medal"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(skiJumpMedal(125.0, 58.0, 0.0, 6.0), "Gold")
        self.assertEqual(skiJumpMedal(119.0, 50.0, 1.0, 4.0), "Bronze")
        self.assertEqual(skiJumpMedal(122.0, 52.0, -1.0, 4.0), "Silver")
        self.assertEqual(skiJumpMedal(118.0, 50.5, -1.5, 4.0), "No Medal")
        self.assertEqual(skiJumpMedal(124.0, 50.5, 2.0, 5.0), "Gold")
        self.assertEqual(skiJumpMedal(119.0, 49.5, 0.0, 3.0), "No Medal")


if __name__ == "__main__":

    unittest.main(verbosity=2)
