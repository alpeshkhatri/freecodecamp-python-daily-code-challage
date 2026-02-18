import unittest

# 2026 Winter Games Day 13: Nordic Combined
# Given an array of jump scores for athletes, calculate their start delay times for the cross-country portion of the Nordic Combined.
# The athlete with the highest jump score starts first (0 second delay). All other athletes start later based on how far behind their jump score is compared to the best jump.
# To calculate the delay for each athlete, subtract the athlete's jump score from the best overall jump score and multiply the result by 1.5. Round the delay up to the nearest integer.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def calculate_start_delays(args):
    logging.debug(f"start of calculate_start_delays {args=}")
    best_score = max(args)
    ret = []
    for i in args:
        delay = (best_score - i) * 1.5
        logging.debug(f"{(i,delay)=}")
        delay_round = round(delay)
        if delay_round % 2 == 0 and (delay - delay_round) == 0.5:  ## not IEEE 754
            delay_round += 1
        logging.debug(f"{(i,delay_round)=}")
        ret.append(delay_round)
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(calculate_start_delays([120, 110, 125]), [8, 23, 0])
        self.assertEqual(calculate_start_delays([118, 125, 122, 120]), [11, 0, 5, 8])
        self.assertEqual(
            calculate_start_delays([100, 105, 95, 110, 120, 115, 108]),
            [30, 23, 38, 15, 0, 8, 18],
        )
        self.assertEqual(
            calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124]),
            [3, 11, 6, 18, 21, 15, 8, 26, 0, 12],
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
