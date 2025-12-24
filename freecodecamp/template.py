import unittest

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def myfunction(args):
    logging.debug('start of function')
    return 'ret'

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(myfunction('args'), 'ret')

if __name__ == '__main__':

    unittest.main(verbosity=2)


