import sys
from pathlib import Path
from colorama import init, Fore, Style

init()

BRANCH_MID = "├── "
BRANCH_END = "└── "
VERTICAL_LINE = "│   "
EMPTY_SPACE = "    "
FOLDER_EMOJI = "📁"
FILE_EMOJI = "📄"


def sort_key(entry):
    """
    Return sorting key to prioritize directories over files and sort by name case-insensitively.
    """
    is_file = entry.is_file()
    name = entry.name.lower()
    return (is_file, name)


def print_directory_tree(path: Path, indent: str = "") -> None:
    """
    Recursively prints directory tree structure with colored output.
    Uses ASCII characters to visualize branches.

    :param path: Path object pointing to a directory.
    :param indent: Current indentation level (used for recursion).
    """
    try:
        entries = sorted(path.iterdir(), key=sort_key)
        entries_count = len(entries)
        for idx, entry in enumerate(entries):
            connector = BRANCH_END if idx == entries_count - 1 else BRANCH_MID
            if entry.is_dir():
                print(
                    f"{indent}{connector}{Fore.BLUE}{FOLDER_EMOJI} {entry.name}{Style.RESET_ALL}/"
                )
                extension = EMPTY_SPACE if idx == entries_count - 1 else VERTICAL_LINE
                print_directory_tree(entry, indent + extension)
            else:
                print(
                    f"{indent}{connector}{Fore.GREEN}{FILE_EMOJI} {entry.name}{Style.RESET_ALL}"
                )
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission denied]: {path}{Style.RESET_ALL}")
    except OSError as e:
        print(f"{indent}{Fore.RED}[OS error]: {e}{Style.RESET_ALL}")


def main():
    """
    Main function: parses command line argument, validates path,
    and prints directory tree.
    """

    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python3 main.py /path/to/directory")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    if not target_path.exists():
        print(f"{Fore.RED}Error: Path does not exist.{Style.RESET_ALL}")
        sys.exit(1)
    if not target_path.is_dir():
        print(f"{Fore.RED}Error: Path is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print(
        f"{Fore.MAGENTA}{Style.BRIGHT}Directory structure of: {target_path}{Style.RESET_ALL}\n"
    )
    print_directory_tree(target_path)


if __name__ == "__main__":
    main()
