import unittest

# 2026 Winter Games Day 5: Cross-Country Skiing
# Given an array of finish times for a cross-country ski race, convert them into times behind the winner.
#
# Given times are strings in "H:MM:SS" format.
# Given times will be in order from fastest to slowest.
# The winners time (fastest time) should correspond to "0".
# Each other time should show the time behind the winner, in the format "+M:SS".
# For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"].
#
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


def calculate_seconds(hms):
    hours, minutes, seconds = hms.split(":")
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    logging.debug(f"{hms=} {hours=} {minutes=} {seconds=}")
    return hours * 60 * 60 + minutes * 60 + seconds


def calulate_hms(seconds):
    logging.debug(seconds)
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds - (minutes * 60)
    else:
        minutes = 0 
    ret = f"{minutes}:{seconds:02}"
    logging.debug(ret)
    return ret


def get_relative_results(args):
    logging.debug(f"start of get_relative_results {args=}")
    seconds = list(map(lambda x: calculate_seconds(x), args))
    logging.debug(f"{seconds=}")
    ret = ["0"]
    for i in  seconds[1:]:
        ret.append("+" + calulate_hms(i - seconds[0]))
    return ret


class TestCodeChallenge(unittest.TestCase):
    def test_daily_coding_challenge(self):
        self.assertEqual(
            get_relative_results(["1:25:32", "1:26:10", "1:27:05"]),
            ["0", "+0:38", "+1:33"],
        )
        self.assertEqual(
            get_relative_results(["1:00:01", "1:00:05", "1:00:10"]),
            ["0", "+0:04", "+0:09"],
        )
        self.assertEqual(
            get_relative_results(["1:10:06", "1:10:23", "1:10:48", "1:12:11"]),
            ["0", "+0:17", "+0:42", "+2:05"],
        )
        self.assertEqual(
            get_relative_results(
                [
                    "0:49:13",
                    "0:49:15",
                    "0:50:14",
                    "0:51:30",
                    "0:51:58",
                    "0:52:16",
                    "0:53:12",
                    "0:53:31",
                    "0:56:19",
                    "1:02:20",
                ]
            ),
            [
                "0",
                "+0:02",
                "+1:01",
                "+2:17",
                "+2:45",
                "+3:03",
                "+3:59",
                "+4:18",
                "+7:06",
                "+13:07",
            ],
        )
        self.assertEqual(
            get_relative_results(
                [
                    "2:01:15",
                    "2:10:45",
                    "2:10:53",
                    "2:11:04",
                    "2:11:55",
                    "2:13:27",
                    "2:14:30",
                    "2:15:10",
                ]
            ),
            ["0", "+9:30", "+9:38", "+9:49", "+10:40", "+12:12", "+13:15", "+13:55"],
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)
