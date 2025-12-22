import unittest

# December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.
# 
# Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:
# 
# Latitude	Daylight Hours
# -90	24
# -75	23
# -60	21
# -45	15
# -30	13
# -15	12
# 0	12
# 15	11
# 30	10
# 45	9
# 60	6
# 75	2
# 90	0
# If the given latitude does not exactly match a table entry, use the value of the closest latitude.
# 
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def daylight_hours(latitude):
    logging.debug('start daylight_hours')
    mapping = { -90:24 ,-75:23 ,-60:21 ,-45:15 ,-30:13 ,-15:12 ,0:12 ,15:11 ,30:10 ,45:9 ,60:6 ,75:2 ,90:0 }
    ret = mapping[round(latitude/15)*15]
    logging.debug(f"{latitude} : {ret}")
    return ret

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(daylight_hours(45) , 9)
        self.assertEqual(daylight_hours(0) , 12)
        self.assertEqual(daylight_hours(-90) , 24)
        self.assertEqual(daylight_hours(-10) , 12)
        self.assertEqual(daylight_hours(23) , 10)
        self.assertEqual(daylight_hours(88) , 0)
        self.assertEqual(daylight_hours(-33) , 13)
        self.assertEqual(daylight_hours(70) , 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)


