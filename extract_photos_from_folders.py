import os
import shutil

def copy_images(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                source_file_path = os.path.join(root, file)
                shutil.copy(source_file_path, destination_folder)

source_directory = 'source'
destination_directory = 'data/photo'

copy_images(source_directory, destination_directory)