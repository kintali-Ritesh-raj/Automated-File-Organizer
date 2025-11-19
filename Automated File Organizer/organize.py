import os
import shutil
from pathlib import Path

# -------- File Categories --------
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".m4a", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".cpp", ".c", ".js", ".html", ".css", ".java"],
}


# -------- Get Category for Each File --------
def get_category(file_path):
    ext = file_path.suffix.lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"


# -------- Ensure Safe Filename (Avoid Overwrite) --------
def safe_move_path(dest_path):
    """If file exists, rename with (1), (2), etc."""
    if not dest_path.exists():
        return dest_path

    parent = dest_path.parent
    filename = dest_path.stem
    ext = dest_path.suffix

    counter = 1
    while True:
        new_path = parent / f"{filename}({counter}){ext}"
        if not new_path.exists():
            return new_path
        counter += 1


# -------- Organize the Folder --------
def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("❌ Folder does not exist.")
        return

    print(f"\n📁 Organizing: {folder}\n")

    for file in folder.iterdir():
        if file.is_dir():
            continue  # Skip folders

        category = get_category(file)
        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        new_location = safe_move_path(category_folder / file.name)

        shutil.move(str(file), str(new_location))
        print(f"✔ Moved: {file.name} → {category}/")

    print("\n🎉 Done! Your folder is now organized.")


# -------- Main Program --------
if __name__ == "__main__":
    path = input("Enter the folder path to organize: ")
    organize_folder(path)
