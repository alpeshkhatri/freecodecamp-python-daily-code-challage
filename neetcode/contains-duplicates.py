from typing import List
import unittest

# Given an integer array return try if any value appears at least twice

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool :
        logging.debug("starting function")
        mset = set()
        for n in nums:
            logging.debug(f"{mset=}")
            if n in mset:
                return True
            mset.add(n)
        return False


class TestCodeChallege(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_containsDuplicate(self): 
        self.assertEqual(self.sol.containsDuplicate([1,2,3]), False)
        self.assertEqual(self.sol.containsDuplicate([1,2,2]), True)

if __name__ == '__main__':
    unittest.main(verbosity=2)


