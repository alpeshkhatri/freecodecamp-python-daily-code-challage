import unittest


# Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.
# For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:
# 2 and 8 (2 + 8 = 10), whose indices are 0 and 4
# 4 and 6 (4 + 6 = 10), whose indices are 2 and 3
# Add all the indices together to get a return value of 9.


import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def pairwise(arr, target):
    logging.debug('start pairwise')
    length = len(arr)
    index_list = set()
    for i in range(0,length):
        for j in range(i+1,length):
            if arr[i] + arr[j] == target :
                index_list.add(i)
                index_list.add(j)
                logging.debug(f"{arr=} {index_list=}")
    return sum(index_list)

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(pairwise([2, 3, 4, 6, 8], 10) , 9)
        self.assertEqual(pairwise([4, 1, 5, 2, 6, 3], 7) , 15)
        self.assertEqual(pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20) , 22)
        self.assertEqual(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24) , 10)


if __name__ == '__main__':

    unittest.main(verbosity=2)


