import sys
from pathlib import Path
from colorama import Fore


def make_directory_tree(directory_path, indent=""):
    global folder_tree
    if directory_path.is_dir():
        folder_tree += f"{Fore.BLUE}{indent} 📁 {directory_path.name}\n"
        for item in directory_path.iterdir():
            if item.is_dir():
                make_directory_tree(item, indent + "  ")
            else:
                folder_tree += f"{Fore.GREEN} {indent}    📄 {item.name}\n"


if __name__ == "__main__":
    try:
        folder_name = Path(sys.argv[1])  # path to folder from user
        folder_tree = ""
        make_directory_tree(folder_name)
        print(folder_tree)
    except:
      print('Please, add path to folder')
