import unittest

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def is_flat(args) -> bool:
    logging.debug(f"start of is_flat {args=}")
    for s in args:
        if isinstance(s, list):
            return False
    return True


# javascript equivalent
# function isFlat(args) {
#   console.debug("start of isFlat", { args });
#   for (const s of args) {
#    if (Array.isArray(s)) {
#      return false;
#    }
#   }
#   return true;
# }


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(is_flat([1, 2, 3, 4]), True)
        self.assertEqual(is_flat([1, [2, 3], 4]), False)
        self.assertEqual(is_flat([1, 0, False, True, "a", "b"]), True)
        self.assertEqual(is_flat(["a", [0], "b", True]), False)
        self.assertEqual(is_flat([1, [2, [3, [4, [5]]]], 6]), False)


if __name__ == "__main__":

    unittest.main(verbosity=2)
