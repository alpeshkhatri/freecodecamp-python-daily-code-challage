import unittest
# 
# Groundhog Day
# Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.
# 
# Given a value representing the groundhog's appearance, return the correct prediction:
# 
# If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
# If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
# If the value is anything else (the groundhog did not show up), return "No prediction this year.".
# 
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def groundhog_day_prediction(args):
    logging.debug(f"start of groundhog_day_prediction {args=}")
    if isinstance(args,bool):
        if args:
            return "Looks like we'll have six more weeks of winter."
        else:
            return "It's going to be an early spring."
    else:
        return "No prediction this year."


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(groundhog_day_prediction(True) , "Looks like we'll have six more weeks of winter.")
        self.assertEqual(groundhog_day_prediction(False) , "It's going to be an early spring.")
        self.assertEqual(groundhog_day_prediction(None) , "No prediction this year.")
        self.assertEqual(groundhog_day_prediction(" ") , "No prediction this year.")
        self.assertEqual(groundhog_day_prediction("True") , "No prediction this year.")


if __name__ == "__main__":

    unittest.main(verbosity=2)
