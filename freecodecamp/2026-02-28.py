import unittest

# Add Punctuation
# Given a string of sentences with missing periods, add a period (".") in the following places:
#
# Before each space that comes immediately before an uppercase letter
# And at the end of the string
# Return the resulting string.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def add_punctuation(args: str) -> str:
    logging.debug(f"start of add_punctuation {args=}")
    ret = args.split()[0]
    rest = args.split()[1:]
    for s in rest:
        if s[0].isupper():
            ret += ". " + s
        else:
            ret += " " + s
    return ret + "."


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(add_punctuation("Hello world"), "Hello world.")
        self.assertEqual(
            add_punctuation("Hello world It's nice today"),
            "Hello world. It's nice today.",
        )
        self.assertEqual(
            add_punctuation("JavaScript is great Sometimes"),
            "JavaScript is great. Sometimes.",
        )
        self.assertEqual(
            add_punctuation("A b c D e F g h I J k L m n o P Q r S t U v w X Y Z"),
            "A b c. D e. F g h. I. J k. L m n o. P. Q r. S t. U v w. X. Y. Z.",
        )
        self.assertEqual(add_punctuation("Wait.. For it"), "Wait... For it.")


if __name__ == "__main__":

    unittest.main(verbosity=2)
