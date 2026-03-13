import unittest

# Domino Chain Validator
# Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.
#
# Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
# For the chain to be valid, the second number of each domino must match the first number of the next domino.
# The first number of the first domino and the last number of the last domino don't need to match anything.
#
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def is_valid_domino_chain(args):
    logging.debug(f"start of is_valid_domino_chain {args=}")
    for i in range(len(args) - 1):
        if args[i][1] != args[i + 1][0]:
            return False
    return True


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(is_valid_domino_chain([[1, 3], [3, 6], [6, 5]]), True)
        self.assertEqual(is_valid_domino_chain([[6, 2], [3, 4], [4, 1]]), False)
        self.assertEqual(is_valid_domino_chain([[2, 5], [5, 6], [5, 1]]), False)
        self.assertEqual(
            is_valid_domino_chain(
                [
                    [4, 3],
                    [3, 1],
                    [1, 6],
                    [6, 6],
                    [6, 5],
                    [5, 1],
                    [1, 1],
                    [1, 4],
                    [4, 4],
                    [4, 2],
                ]
            ),
            True,
        )
        self.assertEqual(
            is_valid_domino_chain(
                [
                    [2, 3],
                    [3, 3],
                    [3, 6],
                    [6, 1],
                    [1, 4],
                    [3, 5],
                    [5, 5],
                    [5, 4],
                    [4, 2],
                    [2, 2],
                ]
            ),
            False,
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
