import os
import shutil

print("PROGRAM STARTED")

# Ask user for folder path
folder_path = input("Enter folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Archives": [".zip", ".rar"],
    "Music": [".mp3", ".wav"],
    "Code": [".py", ".js", ".html", ".css"]
}

# Create category folders
for category in file_types:
    category_path = os.path.join(folder_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Move files to their category
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(filename)[1].lower()

    moved = False
    for category, extensions in file_types.items():
        if extension in extensions:
            shutil.move(file_path, os.path.join(folder_path, category))
            moved = True
            break

    if not moved:
        other_path = os.path.join(folder_path, "Others")
        if not os.path.exists(other_path):
            os.makedirs(other_path)
        shutil.move(file_path, other_path)

print("🎉 Folder Organized Successfully!")
