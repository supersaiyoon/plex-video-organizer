import os

IGNORE_DIRS = [
    "anime",
    "movies",
    "stand-up comedy",
    "tv shows"
    ]

IGNORE_FILE_EXT = [
    ".py"
    ]

TV_SHOWS = [
    "Abbott Elementary",
    "St. Denis Medical",
    ]

ROOT_DIR = "V:/"

def is_ignored_dir(item: str) -> bool:
    return True

def main():
    # Get all contents in root drive
    root_contents_list = os.listdir(ROOT_DIR)
    
    # TODO: How to handle video files in folders vs. not in folder? Separate content list further to dirs and files?
    # Or move video files to root folder? What about subtitle files?

    # TODO: Rename video file

    # TODO: Move video file to final destination folder

if __name__ == "__main__":
    main()