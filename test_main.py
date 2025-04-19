import os
import pytest

from main import IGNORE_DIRS as PLEX_DIRS_LIST, is_valid_item

FAKE_ROOT = "/V"

FAKE_VIDEO_FILES_LIST = [
    # "Abbott Elementary (2021) - S03E13.1080p.mkv"
    "Abbott.Elementary.S03E13.1080p.WEB.H264-SuccessfulCrab[TGx].mkv",
    # "St. Denis Medical (2024) - S01E02.1080p.mkv"
    "St.Denis.Medical.S01E02.1080p.x265-ELiTE.mkv"
]

FAKE_OTHER_FILES_LIST = [
    "_extract_srt_from_mkv.py",
    "_rename_files.py"
]

@pytest.fixture
def vfs(fs):    
    # Create root
    fs.create_dir(FAKE_ROOT)

    # Populate with dirs used by Plex, which should be ignored by this script
    for d in PLEX_DIRS_LIST:
        fs.create_dir(os.path.join(FAKE_ROOT, d))

    # TODO: Populate with fake video files inside folders to be processed

    # Populate with fake video and other files in root to be processed
    for f in FAKE_VIDEO_FILES_LIST + FAKE_OTHER_FILES_LIST:
        fs.create_file(os.path.join(FAKE_ROOT, f))

    return fs

def test_vfs_contains_plex_dirs_and_files(vfs):
    # Populate set of expected fake root structure
    expected_vfs_struct = set(PLEX_DIRS_LIST) | set(FAKE_VIDEO_FILES_LIST) | set(FAKE_OTHER_FILES_LIST)

    vfs_struct = set(os.listdir(FAKE_ROOT))

    assert vfs_struct == expected_vfs_struct

def test_is_valid_item():
    for d in PLEX_DIRS_LIST:
        assert not is_valid_item(d)

def test_valid_item_not_in_ignore_list():
    assert is_valid_item("some_random_folder")

# TODO: Implement pyfakefs to imitate files/folders