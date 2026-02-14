import unittest

# 2026 Winter Games Day 9: Skeleton
# Given a string representing the curves on a skeleton track, determine the difficulty of the track.
#
# The given string will only consist of the letters:
#
# "L" for a left turn
# "R" for a right turn
# "S" for a straight segment
# Each direction change adds 15 points (an "L" followed by an "R" or vice versa).
#
# All other curves add 5 points each (all other "L" or "R" characters).
#
# Straight segments add 0 points.
#
# The difficulty of the track is based on the total score. Return:
#
# "Easy" if the total is 0 - 100
# "Medium" if the total is 101-200
# "Hard" if the total is over 200


import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def get_difficulty(args):
    logging.debug(f"start of get_difficulty {args=}")
    curves_points = 0 
    previous_turn = 'S'
    for i in args :
        if i == 'L' or i == 'R' :
            if previous_turn != i and previous_turn == 'L' or previous_turn == 'R' :
                curves_points += 15
            else:
                curves_points += 5
        previous_turn = i

    # curves_points = (args.count('LR') + args.count('RL') ) * 15
    # logging.debug(f"{curves_points=}")
    # args = args.replace('LR','L').replace('RL','R')
    # logging.debug(f"{args=}")
    # curves_points = curves_points + ( args.count('L') + args.count('R') ) * 5
    # logging.debug(f"{curves_points=}")
    if 0 <= curves_points <= 100 :
        return "Easy"
    elif 101 <= curves_points <= 200 :
        return "Medium"
    else:
        return "Hard"


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_difficulty("SLSLLSRRLSRLRL"), "Easy")
        self.assertEqual(get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS"), "Hard")
        self.assertEqual(get_difficulty("SRRRRLSLLRLRSSRLSRL"), "Medium")
        self.assertEqual(get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL"), "Hard")
        self.assertEqual(get_difficulty("SLLSSLRLSLSLRSLSSLRL"), "Medium")
        self.assertEqual(get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR"), "Easy")


if __name__ == "__main__":

    unittest.main(verbosity=2)
