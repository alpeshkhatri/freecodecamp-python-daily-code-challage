import collections
import unittest
from typing import List


# Description

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool :
        logging.debug("starting isValidSudoku")
        cols = collections.defaultdict(set) 
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key (r/3, c/3)
        for r in range(9):
            for c in range(9):
                logging.debug(f"{r=} {c=}")
                logging.debug(f"{cols=}")
                logging.debug(f"{rows=}")
                logging.debug(f"{squares=}")
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True


class TestCodeChallenge(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_isValidSudoku(self): 
        self.assertEqual(self.sol.isValidSudoku([[3, 9, 7, 1, 6, 8, 5, 2, 4],
                                                 [6, 5, 4, 3, 2, 7, 8, 9, 1],
                                                 [8, 1, 2, 4, 5, 9, 7, 6, 3],
                                                 [2, 3, 1, 7, 8, 6, 9, 4, 5],
                                                 [5, 6, 8, 2, 9, 4, 1, 3, 7],
                                                 [4, 7, 9, 5, 1, 3, 6, 8, 2],
                                                 [9, 4, 3, 8, 7, 1, 2, 5, 6],
                                                 [7, 8, 5, 6, 3, 2, 4, 1, 9],
                                                 [1, 2, 6, 9, 4, 5, 3, 7, 8]]), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)


