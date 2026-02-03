import unittest

# String Mirror
# Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def mirror(args):
    logging.debug(f"start of mirror {args=}")
    return args + args[::-1]


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(mirror("freeCodeCamp"), "freeCodeCamppmaCedoCeerf")
        self.assertEqual(mirror("RaceCar"), "RaceCarraCecaR")
        self.assertEqual(mirror("helloworld"), "helloworlddlrowolleh")
        self.assertEqual(
            mirror("The quick brown fox..."),
            "The quick brown fox......xof nworb kciuq ehT",
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
