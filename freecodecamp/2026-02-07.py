import unittest

# 2026 Winter Games Day 2: Snowboarding
# Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.
#
# A snowboarder's stance is either "Regular" or "Goofy".
# Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
# The landing stance flips every 180 degrees of rotation.
# For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy".

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

flip = {"Regular": "Goofy", "Goofy":"Regular"}

def get_landing_stance(start_stance, rotation):
    logging.debug(f"start of get_landing_stance {start_stance=} {rotation=} ")
    if int(rotation/180) % 2 == 0 :
        return start_stance
    else:
        return flip[start_stance]


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_landing_stance("Regular", 90), "Regular")
        self.assertEqual(get_landing_stance("Regular", 180), "Goofy")
        self.assertEqual(get_landing_stance("Goofy", -270), "Regular")
        self.assertEqual(get_landing_stance("Regular", 2340), "Goofy")
        self.assertEqual(get_landing_stance("Goofy", 2160), "Goofy")
        self.assertEqual(get_landing_stance("Goofy", -540), "Regular")


if __name__ == "__main__":

    unittest.main(verbosity=2)
