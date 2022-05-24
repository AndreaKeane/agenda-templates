from pathlib import Path
import sys
from datetime import datetime, timedelta

def main(date_string, all_files):
    """ """
    # Make parent directory
    path = Path('/Users/akeane/Documents/weeklies') / date_string
    path.mkdir(parents=False, exist_ok=False)
    print(f"Created new directory at: \n\t{path}")

    # Make files
    if all_files:
        standup_file(path, date_string)
        # hnfs_file(path, date_string)
        # okr_files(path)

def hnfs_file(path, date_string):
    """Create a hnfs-yyyymmdd markdown file with standardized contents"""

    # Determine dates for days of the week
    def format_days(n):
        # Add n days, format like Mon 01/06/20 for each day of the week
        return (date_object + timedelta(days=n)).strftime('%a %x')

    date_object = datetime.strptime(date_string, "%Y%m%d")
    days = [format_days(n) for n in [0, 1, 2, 3, 4]]

    # Set up string to write as file contents

    contents = ("# HNFS  \n\n") + ''.join(
        [
            (f"## {date}  \n\n"
            "Updates  \n\n"
            "- \n- \n\n"
            "Notes  \n\n"
            "- \n- \n\n"
            "New Action Items  \n\n"
            "- \n- \n\n") for date in days]
    ) + (
        "## Parking Lot Tasks  \n"
    )

    # Create and write to the file
    create_write_file(path, f"hnfs-{date_string}.md", contents)

def standup_file(path, date_string):
    """Create a standup-yyyymmdd markdown file with standardized contents"""

    # Determine dates for days of the week
    def format_days(n):
        # Add n days, format like Mon 01/06/20 for each day of the week
        return (date_object + timedelta(days=n)).strftime('%a %x')

    date_object = datetime.strptime(date_string, "%Y%m%d")
    days = [format_days(n) for n in [0, 1, 2, 3, 4]]

    # Set up string to write as file contents

    contents = ("# Standup  \n\n") + ''.join(
        [
            (f"## {date}  \n\n"
            "Yesterday  \n\n"
            "- \n- \n\n"
            "Today  \n\n"
            "- \n- \n\n"
            "SI  \n\n"
            "- \n\n") for date in days]
    ) + (
        "## Parking Lot Tasks  \n"
    )

    # Create and write to the file
    create_write_file(path, f"standup-{date_string}.md", contents)


def okr_files(path):
    """ """

    contents = (
        "# OKR  \n\n"
        "*What*  \n"
        "1. \n"
        "2. \n\n"
        "*Measurable*  \n"
        "1. \n"
        "2. \n\n"
        "*Why*  \n"
        "1. \n"
        "2. \n\n"
    )

    create_write_file(path, f"okr-{date_string}.md", contents)


def create_write_file(path, fname, contents):
    """ """
    with (path / fname).open(mode='w') as file:
        file.write(contents)
    print(f"Created new file at: \n\t{path / fname}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Expected Usage: python3 weekly_notes.py 20200106"
            "Date should be a monday, in format yyyymmdd"
        )
    date_string = sys.argv[1]
    all_files = True  # incomplete feature
    main(date_string, all_files)