import unittest

# Zodiac Finder
# Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:
#
# Date Range	Zodiac Sign
# March 21 - April 19	"Aries"
# April 20 - May 20	"Taurus"
# May 21 - June 20	"Gemini"
# June 21 - July 22	"Cancer"
# July 23 - August 22	"Leo"
# August 23 - September 22	"Virgo"
# September 23 - October 22	"Libra"
# October 23 - November 21	"Scorpio"
# November 22 - December 21	"Sagittarius"
# December 22 - January 19	"Capricorn"
# January 20 - February 18	"Aquarius"
# February 19 - March 20	"Pisces"
# Zodiac signs are based only on the month and day, you can ignore the year.
#

import logging
import datetime
import re

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

data = """
March 21 - April 19	"Aries"
April 20 - May 20	"Taurus"
May 21 - June 20	"Gemini"
June 21 - July 22	"Cancer"
July 23 - August 22	"Leo"
August 23 - September 22	"Virgo"
September 23 - October 22	"Libra"
October 23 - November 21	"Scorpio"
November 22 - December 21	"Sagittarius"
December 22 - January 19	"Capricorn"
January 20 - February 18	"Aquarius"
February 19 - March 20	"Pisces"
""".strip().splitlines()

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

global_data = {}
for line in data :
    start_month, start_day, end_month, end_day, zodiac ,_ = re.split(r'[\s\"-]+',line)
    start_date = datetime.datetime(1900,months.index(start_month) + 1,int(start_day))
    end_date   = datetime.datetime(1900,months.index(end_month) + 1,int(end_day))
    if start_date.month == 12 :## rolling over to next year.
        global_data[(start_date,datetime.datetime(1900,12,31))] = zodiac
        global_data[(datetime.datetime(1900,1,1),datetime.datetime(1900,end_date.month,end_date.day))] = zodiac
    else :
        global_data[(start_date,end_date)] = zodiac

logging.debug(global_data)

def get_sign(args):
    logging.debug(f"start of get_sign {args=}")
    year, month , day = args.split("-")
    birthday = datetime.datetime(1900,int(month),int(day))
    for k,v in global_data.items():
        if k[0] <= birthday <= k[1]:
            return v
    return None


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(get_sign("2026-01-31"), "Aquarius")
        self.assertEqual(get_sign("2001-06-10"), "Gemini")
        self.assertEqual(get_sign("1985-09-07"), "Virgo")
        self.assertEqual(get_sign("2023-03-19"), "Pisces")
        self.assertEqual(get_sign("2045-11-05"), "Scorpio")
        self.assertEqual(get_sign("1985-12-06"), "Sagittarius")
        self.assertEqual(get_sign("2025-12-30"), "Capricorn")
        self.assertEqual(get_sign("2018-10-08"), "Libra")
        self.assertEqual(get_sign("1958-05-04"), "Taurus")
        self.assertEqual(get_sign("2025-01-01"), "Capricorn")

if __name__ == "__main__":

    unittest.main(verbosity=2)
