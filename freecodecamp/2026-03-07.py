import unittest

# HSL Validator
# Given a string, determine whether it is a valid CSS hsl() color value.
#
# A valid HSL value must be in the format "hsl(h, s%, l%)", where:
#
# h (hue) must be a number between 0 and 360 (inclusive).
# s (saturation) must be a percentage between 0% and 100%.
# l (lightness) must be a percentage between 0% and 100%.
# Spaces are only allowed:
#
# After the opening parenthesis
# Before and/or after the commas
# Before and/or after closing parenthesis
# Optionally, the value can end with a semi-colon (";").
#
# For example, "hsl(240, 50%, 50%)" is a valid HSL value.

import logging
import re

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def is_valid_hsl(args):
    logging.debug(f"start of is_valid_hsl {args=}")
    t = re.findall(r"hsl\((\s*\d+\s*),(\s*\d+%\s*),(\s*\d+%\s*)\)", args)
    logging.debug(f"{t=}")
    if t == []:
        return False
    else:
        (h, s, l) = t[0]
        h = int(h.strip())
        s = int(s.strip()[:-1])
        l = int(l.strip()[:-1])
        logging.debug(f"{(h,s,l)=}")
        if (0 <= h <= 360) and (0 <= s <= 100) and (0 <= l <= 100):
            return True
        else:
            return False


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(is_valid_hsl("hsl(240, 50%, 50%)"), True)
        self.assertEqual(is_valid_hsl("hsl( 200 , 50% , 75% )"), True)
        self.assertEqual(is_valid_hsl("hsl(99,60%,80%);"), True)
        self.assertEqual(is_valid_hsl("hsl(0, 0%, 0%) ;"), True)
        self.assertEqual(is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;"), True)
        self.assertEqual(is_valid_hsl("hsl(361, 50%, 80%)"), False)
        self.assertEqual(is_valid_hsl("hsl(300, 101%, 70%)"), False)
        self.assertEqual(is_valid_hsl("hsl(200, 55%, 75)"), False)
        self.assertEqual(is_valid_hsl("hsl (80, 20%, 10%)"), False)


if __name__ == "__main__":

    unittest.main(verbosity=2)
