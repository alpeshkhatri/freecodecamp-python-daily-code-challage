import unittest

# Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.
# 
# The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
# Each array item you want to purchase will be in the same format.
# Use the following exchange rates to convert values:
# 
# Currency	1 Unit Equals
# USD	1.00 USD
# EUR	1.10 USD
# GBP	1.25 USD
# JPY	0.0070 USD
# CAD	0.75 USD
# If you can afford all the items in the list, return "Buy them all!".
# Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.
# 
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def convert_to_usd(amount,currency) :
    rate = { "USD":	1.00 , "EUR":	1.10 , "GBP":	1.25 , "JPY":	0.0070 , "CAD":	0.75 }
    return amount*rate[currency]

def buy_items(funds, items):
    logging.debug('start buy_items')
    fund_usd = convert_to_usd(float(funds[0]),funds[1]) 
    logging.debug(f"{fund_usd=}")
    items_usd = [ convert_to_usd(float(n),c) for n,c in items]
    logging.debug(f"{items_usd=}")
    for idx, item in enumerate(items_usd) :
        fund_usd = fund_usd - item
        logging.debug(f"{fund_usd=}")
        if fund_usd < 0 :
            return f"Buy the first {idx} items."
    return "Buy them all!"

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(buy_items(["150.00", "USD"], [["50.00", "USD"], ["75.00", "USD"], ["30.00", "USD"]]) , "Buy the first 2 items.")
        self.assertEqual(buy_items(["200.00", "EUR"], [["50.00", "USD"], ["50.00", "USD"]]) , "Buy them all!")
        self.assertEqual(buy_items(["100.00", "CAD"], [["20.00", "USD"], ["15.00", "EUR"], ["10.00", "GBP"], ["6000", "JPY"], ["5.00", "CAD"], ["10.00", "USD"]]) , "Buy the first 3 items.")
        self.assertEqual(buy_items(["5000", "JPY"], [["3.00", "USD"], ["1000", "JPY"], ["5.00", "CAD"], ["2.00", "EUR"], ["4.00", "USD"], ["2000", "JPY"]]) , "Buy them all!")
        self.assertEqual(buy_items(["200.00", "USD"], [["50.00", "USD"], ["40.00", "EUR"], ["30.00", "GBP"], ["5000", "JPY"], ["25.00", "CAD"], ["20.00", "USD"]]) , "Buy the first 5 items.")

if __name__ == '__main__':

    unittest.main(verbosity=2)


