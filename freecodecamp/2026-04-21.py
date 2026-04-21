import unittest

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def get_odd_words(args):
    logging.debug(f"start of get_odd_words {args=}")
    ret = []
    for w in args.split(" "):
        if len(w) % 2 == 1:
            ret.append(w)
    logging.debug(f"{ret=}")
    return " ".join(ret)


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_odd_words("This is a super good test"), "a super")
        self.assertEqual(get_odd_words("one two three four"), "one two three")
        self.assertEqual(
            get_odd_words("banana split sundae with rainbow sprinkles on top"),
            "split rainbow sprinkles top",
        )
        self.assertEqual(
            get_odd_words("The quick brown fox jumped over the lazy river"),
            "The quick brown fox the river",
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
