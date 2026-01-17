import unittest
from typing import List


# Given the array return answer such that answer[i] is equal to the product of all elements of array except num[i]

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def productExceptSelf(self, args: List[int]) -> List[int] :
        logging.debug("starting productExceptSelf")
        res = [1] * (len(args))
        prefix = 1
        for i in range(len(args)):
            res[i] = prefix
            prefix *= args[i]
        postfix = 1
        for i in range(len(args) -1, -1 , -1):
            res[i] *= postfix
            postfix *= args[i]
        return res

class TestCodeChallenge(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_productExceptSelf(self): 
        self.assertEqual(self.sol.productExceptSelf([1,2,3,4]), [24,12,8,6])

if __name__ == '__main__':
    unittest.main(verbosity=2)


