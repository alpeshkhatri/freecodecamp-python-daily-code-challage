from collections import defaultdict
from typing import List
import unittest

# Description

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def groupAnagrams(self, args: List[str]) -> List[List[str]] :
        logging.debug("starting groupAnagrams")
        res = defaultdict(list)
        for s in args:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


class TestCodeChallege(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_groupAnagrams(self): 
        self.assertEqual(self.sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])


if __name__ == '__main__':
    unittest.main(verbosity=2)


