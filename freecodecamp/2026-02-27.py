import unittest

# Matrix Shift
# Given a matrix (array of arrays) of numbers and an integer, shift all values in the matrix by the given amount.
#
# A positive shift moves values to the right.
# A negative shift moves values to the left.
# Values should wrap:
#
# Treat the matrix as one continuous sequence of values.
# When a value moves past the end of a row, it continues at the beginning of the next row.
# When a value moves past the last position in the matrix, it wraps to the first position.
# The same applies in reverse when shifting left.
# For example, given:
#
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# with a shift of 1, move all the numbers to the right one:
#
# [
#   [6, 1, 2],
#   [3, 4, 5]
# ]

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def shift_matrix(args, shift):
    logging.debug(f"start of shift_matrix {(args, shift)=}")
    col_len = len(args)
    row_len = len(args[0])
    shift = shift % (col_len * row_len)
    temp = [c for row in args for c in row]
    temp = temp[-shift:] + temp[: col_len * row_len - shift]
    ret = []
    for i in range(col_len):
        ret.append(temp[row_len * i : (row_len * i) + row_len])
    logging.debug(f"{(col_len,row_len,ret)=}")
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(
            shift_matrix([[1, 2, 3], [4, 5, 6]], 1), [[6, 1, 2], [3, 4, 5]]
        )
        self.assertEqual(
            shift_matrix([[1, 2, 3], [4, 5, 6]], -1), [[2, 3, 4], [5, 6, 1]]
        )
        self.assertEqual(
            shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5),
            [[5, 6, 7], [8, 9, 1], [2, 3, 4]],
        )
        self.assertEqual(
            shift_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -6),
            [[7, 8, 9], [1, 2, 3], [4, 5, 6]],
        )
        self.assertEqual(
            shift_matrix(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 7
            ),
            [[10, 11, 12, 13], [14, 15, 16, 1], [2, 3, 4, 5], [6, 7, 8, 9]],
        )
        self.assertEqual(
            shift_matrix(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], -54
            ),
            [[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 1, 2], [3, 4, 5, 6]],
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
