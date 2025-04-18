import unittest

from main import is_valid_item
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
    def test_is_valid_item(self):
        self.assertEqual(is_valid_item("anime"), False)
        self.assertEqual(is_valid_item("movies"), False)
        self.assertEqual(is_valid_item("stand-up comedy"), False)
        self.assertEqual(is_valid_item("tv shows"), False)

        self.assertEqual(is_valid_item("some_folder"), True)
    
    def test_format_title(self):
        for case in TEST_CASES:
            raw_filename, expected_filename = case
            self.assertEqual(process_file(raw_filename), expected_filename)

# TODO: Implement pyfakefs to imitate files/folders