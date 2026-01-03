import unittest

#
# Left-Handed Seat at the Table
# Given a 4x2 matrix (array of arrays) representing the seating arrangement for a meal, determine how many seats a left-handed person can sit at.
#
# A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.
# In the given matrix:
#
# An "R" is a seat occupied by a right-handed person.
# An "L" is a seat occupied by a left-handed person.
# An "U" is an unoccupied seat.
# Only unoccupied seats are available to sit at.
# The seats in the top row are facing "down", and the seats in the bottom row are facing "up" (like a table), so left and right are relative to the seat's orientation.
# Corner seats only have one seat next to them.
# For example, in the given matrix:
#
# [
#   ["U", "R", "U", "L"],
#   ["U", "R", "R", "R"]
# ]
# The top-left seat is cannot be sat in because there's a right-handed person to the left. The other two open seats can be sat in because there isn't a right-handed person to the left.
#
#
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def find_left_handed_seats_in_row(row):
    logging.debug("start of find_left_handed_seats_in_row")
    ret = 0
    for idx, seat in enumerate(row):
        logging.debug(f"{idx=} {seat=} {row=}")
        if seat == "U":
            if idx == 0:
                ret += 1
            elif row[idx - 1] == "R":
                pass  # cannot seat left person.
            else:
                ret += 1
        else:
            pass  # cannot seat is occupied
    return ret


def find_left_handed_seats(table):
    logging.debug("start of find_left_handed_seats")
    ret = 0
    ret = ret + find_left_handed_seats_in_row(table[0][::-1])
    ret = ret + find_left_handed_seats_in_row(table[1])
    return ret


class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(
            find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]), 2
        )
        self.assertEqual(
            find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]), 8
        )
        self.assertEqual(
            find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]), 0
        )
        self.assertEqual(
            find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]), 1
        )
        self.assertEqual(
            find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]), 5
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
