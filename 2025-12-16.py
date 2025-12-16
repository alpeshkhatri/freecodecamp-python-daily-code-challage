import unittest


"""
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting.

"""

import string
def has_consonant_count(text, target):
    count = 0
    text_lower = text.lower()
    consonants = sorted(set(string.ascii_lowercase) - set(["a", "e", "i", "o", "u"]))
    for c in consonants :
        count += text_lower.count(c)
    return target == count

class TestCodeChallege(unittest.TestCase):
    def test_daily_coding_challenge(self): 
        ## self.assertEqual(has_consonant_count("helloworld", 7) , True)
        self.assertEqual(has_consonant_count("freeCodeCamp Rocks!", 11), True)
if __name__ == '__main__':
    unittest.main(verbosity=2)
