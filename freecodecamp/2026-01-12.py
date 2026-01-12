import unittest

# Plant the Crop
# Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.
# 
# 1 acre equals 4046.86 square meters.
# 1 hectare equals 10,000 square meters.
# Here's a list of crops that will be given as input and how much space a single plant takes:
# Crop	Space per plant
# "corn"	1 square meter
# "wheat"	0.1 square meters
# "soybeans"	0.5 square meters
# "tomatoes"	0.25 square meters
# "lettuce"	0.2 square meters
# Return the number of plants that fit in the field, rounded down to the nearest whole plant.
# 

import logging

space_needed = {    "corn":	1 ,
                    "wheat":	0.1 ,
                    "soybeans":	0.5 ,
                    "tomatoes":	0.25 ,
                    "lettuce":	0.2 }

unit_conversion_multiplier = { "acres" : 4046.86, "hectares": 10000 }

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def get_number_of_plants(field_size, unit, crop):
    logging.debug(f'start of get_number_of_plants')
    field_size_sqmt = field_size * unit_conversion_multiplier[unit]
    number_of_plants = int(field_size_sqmt / space_needed[crop])
    return number_of_plants

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        self.assertEqual(get_number_of_plants(1, "acres", "corn") , 4046)
        self.assertEqual(get_number_of_plants(2, "hectares", "lettuce") , 100000)
        self.assertEqual(get_number_of_plants(20, "acres", "soybeans") , 161874)
        self.assertEqual(get_number_of_plants(3.75, "hectares", "tomatoes") , 150000)
        self.assertEqual(get_number_of_plants(16.75, "acres", "tomatoes") , 271139)

if __name__ == '__main__':
    unittest.main(verbosity=2)


