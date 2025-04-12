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
    return item in IGNORE_DIRS

def process_file(raw_filename: str) -> str:
    # TODO: Split raw filename

    # TODO: Format title and year

    # TODO: Format season and episode `SXXEXX`
    
    # TODO: Append rest of filename (e.g., resolution)

    # TODO: Don't forget extension

    processed_filename = ""

    return processed_filename

def main():
    # Get all contents in root drive
    root_contents_list = os.listdir(ROOT_DIR)
    
    # TODO: How to handle video files in folders vs. not in folder? Separate content list further to dirs and files?
    # Or move video files to root folder? What about subtitle files?

    # TODO: Get single video file

    # TODO: Rename video file to format preferred by Plex

    # TODO: Move video file to final destination folder

if __name__ == "__main__":
    main()