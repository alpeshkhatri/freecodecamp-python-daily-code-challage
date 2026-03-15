import unittest

# Captured Chess Pieces
# Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.
#
# In chess, you start with 16 pieces:
#
# Piece	Abbreviation	Quantity	Value
# Pawn	"P"	8	1
# Rook	"R"	2	5
# Knight	"N"	2	3
# Bishop	"B"	2	3
# Queen	"Q"	1	9
# King	"K"	1	0
# The given array will only contain the abbreviations above.
# Any of the 16 pieces not included in the given array have been captured.
# Return the total value of all captured pieces, unless...
# If the King has been captured, return "Checkmate".


import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def get_captured_value(args):
    logging.debug(f"start of get_captured_value {args=}")
    if "K" not in args:
        return "Checkmate"
    quantity = {"P": 8, "R": 2, "N": 2, "B": 2, "Q": 1, "K": 1}
    value = {"P": 1, "R": 5, "N": 3, "B": 3, "Q": 9, "K": 0}
    for piece in args:
        quantity[piece] -= 1
    logging.debug(f"{quantity=}")
    sum = 0
    for piece, current_quantity in quantity.items():
        sum += current_quantity * value[piece]
    return sum


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(
            get_captured_value(
                ["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"]
            ),
            8,
        )
        self.assertEqual(
            get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]), 26
        )
        self.assertEqual(
            get_captured_value(
                ["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"]
            ),
            16,
        )
        self.assertEqual(
            get_captured_value(
                ["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]
            ),
            4,
        )
        self.assertEqual(get_captured_value(["P", "K"]), 38)
        self.assertEqual(
            get_captured_value(
                [
                    "N",
                    "P",
                    "P",
                    "B",
                    "K",
                    "P",
                    "Q",
                    "N",
                    "P",
                    "P",
                    "R",
                    "R",
                    "P",
                    "P",
                    "P",
                    "B",
                ]
            ),
            0,
        )
        self.assertEqual(
            get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"]),
            "Checkmate",
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
