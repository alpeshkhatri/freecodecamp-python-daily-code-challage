from typing import List
import unittest

# Top K Frequent Elements.

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def topKFrequent(self, args: List[int], k: int) -> List[int] :
        logging.debug("starting topKFrequent")
        count = {}
        freq = [[] for i in range(len(args) + 1)]
        for n in args:
            count[n] = 1 + count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return args


class TestCodeChallege(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_topKFrequent(self): 
        self.assertEqual(self.sol.topKFrequent([1,1,2,2,2,1,3,3,3],2), [1,2])


if __name__ == '__main__':
    unittest.main(verbosity=2)


