import os
import pytest

from main import IGNORE_DIRS
from main import is_valid_item
from main import process_file

FAKE_ROOT = "/V"

PLEX_DIRS_LIST = IGNORE_DIRS

FAKE_VIDEO_FILES_LIST = [
    "Abbott.Elementary.S03E13.1080p.WEB.H264-SuccessfulCrab[TGx].mkv",
    "St.Denis.Medical.S01E02.1080p.x265-ELiTE.mkv"
]

FAKE_OTHER_FILES_LIST = [
    "_extract_srt_from_mkv.py",
    "_rename_files.py"
]

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

    # Populate with dirs used by Plex, which should be ignored by this script
    for dir_name in PLEX_DIRS_LIST:
        fs.create_dir(FAKE_ROOT + "/" + dir_name)

    # TODO: Populate with fake video files inside folders to be processed

    # Populate with fake video files in root to be processed
    for video_filename in FAKE_VIDEO_FILES_LIST:
        fs.create_file(FAKE_ROOT + "/" + video_filename)

    # Populate with non-video files that should be ignored
    for other_filename in FAKE_OTHER_FILES_LIST:
        fs.create_file(FAKE_ROOT + "/" + other_filename)

    return fs

def test_vfs_structure_is_correct(vfs):
    # Populate set of expected fake root structure
    expected_vfs_struct = set(IGNORE_DIRS)
    expected_vfs_struct.update(set(FAKE_VIDEO_FILES_LIST))
    expected_vfs_struct.update(set(FAKE_OTHER_FILES_LIST))

    vfs_struct = os.listdir(FAKE_ROOT)

    assert set(vfs_struct) == expected_vfs_struct

def test_is_valid_item():
    for dir_name in IGNORE_DIRS:
        assert not is_valid_item(dir_name)

def test_valid_item_not_in_ignore_list():
    assert is_valid_item("test_folder")

# TODO: Implement pyfakefs to imitate files/folders