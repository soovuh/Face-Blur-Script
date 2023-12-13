import os

def rename_images_to_lowercase(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, file.lower())
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")

# Provide the path to your main folder containing subfolders with images
folder_path = 'data/photo/photos/'

rename_images_to_lowercase(folder_path)
