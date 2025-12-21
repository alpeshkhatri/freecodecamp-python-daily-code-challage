import unittest

# Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.
# 
# If multiple values are tied for most frequent, remove all of them.
# Do not change any of the other elements or their order.
# 

import logging
from collections import Counter
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def purge_most_frequent(arr):
    logging.debug('start purge_most_frequent')
    most_occuring = Counter(arr).most_common()[0][0]
    logging.debug(most_occuring)
    ret = [i for i in arr if i != most_occuring]
    logging.debug(f"{ret=}")
    return ret

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(purge_most_frequent([1, 2, 2, 3]) , [1, 3])
        self.assertEqual(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]) , ["a", "b", "b", "c", "c", "c"])
        self.assertEqual(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]) , ["red", "green", "red", "green"])
        self.assertEqual(purge_most_frequent([5, 5, 5, 5]) , [])

if __name__ == '__main__':

    unittest.main(verbosity=2)


