import unittest

#  Smallest Gap
#  Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).
#
#  There will always be at least one pair of matching characters.
#  The returned substring should exclude the matching characters.
#  If two or more gaps are the same length, return the characters from the first one.
#  For example, given "ABCDAC", return "DA".
#
#  Only "A" and "C" repeat in the string.
#  The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
#  So return the string between the two "C" characters.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def smallest_gap(args):
    logging.debug(f"start of smallest_gap {args=}")
    seen = {}
    smallest_len = float("inf")
    start, end = 0, 0
    for idx, s in enumerate(args):
        if s in seen:
            length = idx - seen[s]
            if length < smallest_len:
                smallest_len = length
                start, end = seen[s], idx
        seen[s] = idx
    logging.debug(args[start + 1 : end])
    return args[start + 1 : end]


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(smallest_gap("ABCDAC"), "DA")
        self.assertEqual(smallest_gap("racecar"), "e")
        self.assertEqual(
            smallest_gap("A{5e^SD*F4i!o#q6e&rkf(po8|we9+kr-2!3}=4"), "#q6e&rkf(p"
        )
        self.assertEqual(smallest_gap("Hello World"), "")
        self.assertEqual(
            smallest_gap("The quick brown fox jumps over the lazy dog."), "fox"
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
