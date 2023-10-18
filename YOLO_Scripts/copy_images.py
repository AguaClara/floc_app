import os
import shutil
import random

# Source and destination directories
source_dir = "legacy/openCV/flocs"
destination_dir = "YOLO_Scripts/images"

# Number of random images to copy
num_images_to_copy = 100

# Get a list of all files in the source directory
all_files = os.listdir(source_dir)

# Randomly select 50 files from the list (assuming there are at least 50 files)
selected_files = random.sample(all_files, num_images_to_copy)

# Iterate through the selected files and copy them to the destination directory
for filename in selected_files:
    source_path = os.path.join(source_dir, filename)
    destination_path = os.path.join(destination_dir, filename)
    
    # Use shutil.copy to copy the file
    shutil.copy(source_path, destination_path)
    print(f"Copying {filename} to {destination_path}")

print("Copy process completed.")
