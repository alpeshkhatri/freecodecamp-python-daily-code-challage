import unittest

# Truncate the Text
# Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def truncate_text(args):
    logging.debug(f"start of truncate_text {args=}")
    if len(args) <= 20 :
        return args
    else:
        return f"{args[0:17]}..."



class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(truncate_text("Hello, world!") , "Hello, world!")
        self.assertEqual(truncate_text("This string should get truncated.") , "This string shoul...")
        self.assertEqual(truncate_text("Exactly twenty chars") , "Exactly twenty chars")
        self.assertEqual(truncate_text(".....................") , "....................")


if __name__ == "__main__":

    unittest.main(verbosity=2)
