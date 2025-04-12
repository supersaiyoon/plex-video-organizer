import unittest

from main import is_ignored_dir
from main import process_file

TEST_CASES = [
    (
        "Abbott.Elementary.S03E13.1080p.WEB.H264-SuccessfulCrab[TGx].mkv",
        "Abbott Elementary (2021) - S03E13.1080p.mkv"
    ),
    (
        "St.Denis.Medical.S01E02.1080p.x265-ELiTE.mkv",
        "St. Denis Medical (2024) - S01E02.1080p.mkv"
    )
]

class TestMain(unittest.TestCase):
    def test_is_ignored_dir(self):
        self.assertEqual(is_ignored_dir("anime"), True)
        self.assertEqual(is_ignored_dir("movies"), True)
        self.assertEqual(is_ignored_dir("stand-up comedy"), True)
        self.assertEqual(is_ignored_dir("tv shows"), True)

        self.assertEqual(is_ignored_dir("some_folder"), False)
    
    def test_format_title(self):
        for case in TEST_CASES:
            raw_filename, expected_filename = case
            self.assertEqual(process_file(raw_filename), expected_filename)