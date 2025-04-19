import os
import pytest

from main import IGNORE_DIRS
from main import is_valid_item
from main import process_file

FAKE_ROOT = "/V"

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

@pytest.fixture
def vfs(fs):    
    # Create root
    fs.create_dir(FAKE_ROOT)

    # Populate with dirs used by Plex
    plex_dirs_list = ["anime", "movies", "stand-up comedy", "tv shows"]

    for dir_name in plex_dirs_list:
        fs.create_dir(FAKE_ROOT + "/" + dir_name)

    # TODO: Populate with fake video files inside folders to be processed

    # Populate with fake video files in root to be processed
    fake_video_files_list = [
        "Abbott.Elementary.S03E13.1080p.WEB.H264-SuccessfulCrab[TGx].mkv",
        "St.Denis.Medical.S01E02.1080p.x265-ELiTE.mkv"
    ]

    for video_filename in fake_video_files_list:
        fs.create_file(FAKE_ROOT + "/" + video_filename)

    # Populate with non-video files that should be ignored
    fake_other_files_list = [
        "_extract_srt_from_mkv.py",
        "_rename_files.py"
    ]

    for other_filename in fake_other_files_list:
        fs.create_file(FAKE_ROOT + "/" + other_filename)

    return fs

def test_vfs_structure_is_correct(vfs):
    print(os.listdir(FAKE_ROOT))
    pass

def test_is_valid_item():
    for dir_name in IGNORE_DIRS:
        assert not is_valid_item(dir_name)

def test_valid_item_not_in_ignore_list():
    assert is_valid_item("test_folder")

def test_format_title():
    for raw_filename, expected_filename in TEST_CASES:
        assert process_file(raw_filename) == expected_filename

# TODO: Implement pyfakefs to imitate files/folders