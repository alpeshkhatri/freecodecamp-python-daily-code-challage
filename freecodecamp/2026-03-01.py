import unittest

import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def is_flat(args) -> bool:
    logging.debug(f"start of is_flat {args=}")
    for s in args:
        if isinstance(s, list):
            return False
    return True


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(is_flat([1, 2, 3, 4]), True)
        self.assertEqual(is_flat([1, [2, 3], 4]), False)
        self.assertEqual(is_flat([1, 0, False, True, "a", "b"]), True)
        self.assertEqual(is_flat(["a", [0], "b", True]), False)
        self.assertEqual(is_flat([1, [2, [3, [4, [5]]]], 6]), False)


if __name__ == "__main__":

    unittest.main(verbosity=2)

# javascript equivalent
# 
# function isFlat(args) {
#   console.debug(`start of is_flat args=${JSON.stringify(args)}`);
#   for (const s of args) {
#     if (Array.isArray(s)) return false;
#   }
#   return true;
# }
# 
# // Tests
# const tests = [
#   [isFlat([1, 2, 3, 4]), true],
#   [isFlat([1, [2, 3], 4]), false],
#   [isFlat([1, 0, false, true, "a", "b"]), true],
#   [isFlat(["a", [0], "b", true]), false],
#   [isFlat([1, [2, [3, [4, [5]]]], 6]), false],
# ];
# 
# tests.forEach(([result, expected], i) => {
#   const pass = result === expected;
#   console.log(`Test ${i + 1}: ${pass ? "PASS" : "FAIL"}`);
# });
