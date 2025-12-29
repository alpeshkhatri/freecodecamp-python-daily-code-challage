import unittest
from collections import Counter

# Given two strings s and t return true of t is an anagram of s else false

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class Solution:
    def is_anagram(self, s: str, t:str) -> bool :
        logging.debug("starting is_anagram")
        # logging.debug(f"{Counter(s)} {Counter(t)}")
        # return Counter(s) == Counter(t)
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i],0)
            count_t[t[i]] = 1 + count_t.get(t[i],0)
        for c in count_s:
            if count_s[c] != count_t.get(c,0):
                return False
        return True



class TestCodeChallege(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    def tearDown(self):
        self.sol = None
    def test_is_anagram(self): 
        self.assertEqual(self.sol.is_anagram('anagram','nagaram'), True)
        self.assertEqual(self.sol.is_anagram('dog','cat'), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)


