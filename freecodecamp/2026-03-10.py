import unittest

# Array Insertion
# Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def insert_into_array(arr, value, index):
    logging.debug(f"start of insert_into_array {(arr, value, index)=}")
    arr.insert(index, value)
    return arr


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(insert_into_array([2, 4, 8, 10], 6, 2), [2, 4, 6, 8, 10])
        self.assertEqual(
            insert_into_array(["the", "quick", "fox"], "brown", 2),
            ["the", "quick", "brown", "fox"],
        )
        self.assertEqual(insert_into_array([], 0, 0), [0])
        self.assertEqual(
            insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5), [0, 1, 1, 2, 3, 5, 8, 13]
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
