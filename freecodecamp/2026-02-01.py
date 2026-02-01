import unittest

# Digital Detox
# Given an array of your login logs, determine whether you have met your digital detox goal.
#
# Each log is a string in the format "YYYY-MM-DD HH:mm:ss".
#
# You have met your digital detox goal if both of the following statements are true:
#
# You logged in no more than once within any four-hour period.
# You logged in no more than 2 times on any single day.


import logging
import datetime
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def digital_detox(args):
    logging.debug(f"start of digital_detox {args=}")
    login_datetimes = sorted([datetime.datetime.strptime(dt,r"%Y-%m-%d %H:%M:%S") for dt in args], reverse=True)
    logging.debug(login_datetimes)
    login_dates = {}
    previous_login = None
    for dt in login_datetimes :
        login_date = dt.strftime('%Y-%m-%d')
        login_dates[login_date] = login_dates.get(login_date,0) + 1
        logging.debug(login_dates)
        if login_dates[login_date]  > 2 :
            return False
        if previous_login:
            seconds_from_previous_login = (previous_login - dt).total_seconds()
            logging.debug(seconds_from_previous_login)
            if seconds_from_previous_login < 4*60*60 :
                return False
        previous_login = dt
    return True


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(
            digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]), True
        )
        self.assertEqual(
            digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]), False
        )
        self.assertEqual(
            digital_detox(
                [
                    "2026-01-31 08:21:30",
                    "2026-01-31 14:30:00",
                    "2026-02-01 08:00:00",
                    "2026-02-01 12:30:00",
                ]
            ),
            True,
        )
        self.assertEqual(
            digital_detox(
                [
                    "2026-01-31 10:40:21",
                    "2026-01-31 15:19:41",
                    "2026-01-31 21:49:50",
                    "2026-02-01 09:30:00",
                ]
            ),
            False,
        )
        self.assertEqual(
            digital_detox(
                [
                    "2026-02-05 10:00:00",
                    "2026-02-01 09:00:00",
                    "2026-02-03 22:15:00",
                    "2026-02-02 12:10:00",
                    "2026-02-02 07:15:00",
                    "2026-02-04 09:45:00",
                    "2026-02-01 16:50:00",
                    "2026-02-03 09:30:00",
                ]
            ),
            True,
        )
        self.assertEqual(
            digital_detox(
                [
                    "2026-02-05 10:00:00",
                    "2026-02-01 09:00:00",
                    "2026-02-03 22:15:00",
                    "2026-02-02 12:10:00",
                    "2026-02-02 07:15:00",
                    "2026-02-04 01:45:00",
                    "2026-02-01 16:50:00",
                    "2026-02-03 09:30:00",
                ]
            ),
            False,
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
