import unittest

# Description

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def function(self, args: str) -> str :
        logging.debug("starting function")
        return args


class TestCodeChallege(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_function(self): 
        self.assertEqual(self.sol.function('args'), 'args')
        self.assertEqual(self.sol.function('args'), 'args')

if __name__ == '__main__':
    unittest.main(verbosity=2)


