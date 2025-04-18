import pytest

from main import IGNORE_DIRS
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

def test_is_valid_item():
    for dir_name in IGNORE_DIRS:
        assert not is_valid_item(dir_name)

def test_valid_item_not_in_ignore_list():
    assert is_valid_item("test_folder")

def test_format_title():
    for raw_filename, expected_filename in TEST_CASES:
        assert process_file(raw_filename) == expected_filename

# TODO: Implement pyfakefs to imitate files/folders