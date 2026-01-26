import unittest
from typing import List


# Description

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        logging.debug("starting maxProfit")
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit


class TestCodeChallenge(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def tearDown(self):
        self.sol = None

    def test_maxProfit(self):
        self.assertEqual(self.sol.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(
            self.sol.maxProfit([8, 8, 8, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]), 5
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
