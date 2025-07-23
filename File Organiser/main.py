import os
import shutil

# Define file extensions for each category
file_categories = {
    "Audio": ["mp3", "wav"],
    "Video": ["mp4", "mov"],
    "Documents": ["docx", "pptx", "txt","pdf"],
    "Pictures": ["png", "jpg", "jpeg", "webp","svg"],
    "Apps": ["apk","exe"],
    "Compressed":["zip","archive"]

}

# Create directories if they don't exist
for category in file_categories.keys():
    os.makedirs(category, exist_ok=True)

# Function to move files to appropriate directories
def organize_files():
    for file in os.listdir():
        if os.path.isfile(file):
            # Get file extension
            _, ext = os.path.splitext(file)
            ext = ext.lower().lstrip(".")  # Normalize extension
            
            # Find the category for the file
            target_dir = next((category for category, extensions in file_categories.items() if ext in extensions), "Others")
            
            # Move the file to the appropriate directory
            shutil.move(file, os.path.join(target_dir, file))

# Organize files
organize_files()                                                                                       