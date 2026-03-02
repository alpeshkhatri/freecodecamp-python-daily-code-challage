import unittest

# Given a string, return the sum of its letters.
#
# Letters are A-Z in uppercase or lowercase
# Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
# Uppercase and lowercase letters have the same value.
# Ignore all non-letter characters.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def sum_letters(args):
    logging.debug(f"start of sum_letters {args=}")
    sum = 0
    for c in args:
        if c.isalpha():
            sum += 1 + (ord(c.lower()) - ord("a".lower()))
    return sum


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(sum_letters("Hello"), 52)
        self.assertEqual(sum_letters("freeCodeCamp"), 94)
        self.assertEqual(
            sum_letters("The quick brown fox jumps over the lazy dog."), 473
        )
        self.assertEqual(
            sum_letters(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."
            ),
            1681,
        )
        self.assertEqual(sum_letters("</404>"), 0)


if __name__ == "__main__":

    unittest.main(verbosity=2)
