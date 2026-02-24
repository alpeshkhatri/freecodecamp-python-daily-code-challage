import unittest

# Given a start date and an end date, return the number of business days between the two.
#
# Given dates are in the format "YYYY-MM-DD".
# Weekdays are business days (Monday through Friday).
# Weekends are not business days (Saturday and Sunday).
# Include both the start and end dates when counting.

import logging
import datetime

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def count_business_days(start, end):
    logging.debug(f"start of count_business_days {(start, end)=}")
    s = datetime.datetime.strptime(start, "%Y-%m-%d")
    e = datetime.datetime.strptime(end, "%Y-%m-%d")
    c = s
    business_days = 0
    while c <= e:
        if c.weekday() < 5:
            business_days += 1
        c += datetime.timedelta(1)
    return business_days


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(count_business_days("2026-02-24", "2026-02-26"), 3)
        self.assertEqual(count_business_days("2026-02-24", "2026-02-28"), 4)
        self.assertEqual(count_business_days("2026-02-21", "2026-03-01"), 5)
        self.assertEqual(count_business_days("2026-03-08", "2026-03-17"), 7)
        self.assertEqual(count_business_days("2026-02-24", "2027-02-24"), 262)


if __name__ == "__main__":

    unittest.main(verbosity=2)
