import unittest

# Playing Card Values
# Given an array of playing cards, return a new array with the numeric value of each card.
#
# Card Values:
#
# An Ace ("A") has a value of 1.
# Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
# Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
# Suits:
#
# Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
# Card Format:
#
# Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs.
#
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def card_values(args):
    logging.debug(f"start of card_values {args=}")
    values = {"A": 1, "J": 10, "Q": 10, "K": 10}
    ret = []
    for s in args:
        if s[:-1] in values:
            ret.append(values[s[:-1]])
        else:
            ret.append(int(s[:-1]))
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(card_values(["3H", "4D", "5S"]), [3, 4, 5])
        self.assertEqual(
            card_values(["AS", "10S", "10H", "6D", "7D"]), [1, 10, 10, 6, 7]
        )
        self.assertEqual(card_values(["8D", "QS", "2H", "JC", "9C"]), [8, 10, 2, 10, 9])
        self.assertEqual(card_values(["AS", "KS"]), [1, 10])
        self.assertEqual(
            card_values(["10H", "JH", "QH", "KH", "AH"]), [10, 10, 10, 10, 1]
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
