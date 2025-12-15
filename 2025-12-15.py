import unittest

def speed_check(speed_mph, speed_limit_kph):
    speed_kph = speed_mph * 1.60934
    if speed_kph < speed_limit_kph :
        return "Not Speeding"
    elif speed_kph > speed_limit_kph + 5 :
        return "Ticket"
    else:
        return "Warning"

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(speed_check(30,70), 'Not Speeding')
        self.assertEqual(speed_check(40,60), 'Warning')
        self.assertEqual(speed_check(40,65), 'Not Speeding')
        self.assertEqual(speed_check(65,100), 'Warning')


if __name__ == '__main__':
    unittest.main(verbosity=2)
