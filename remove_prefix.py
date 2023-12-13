import os

def remove_blurred_prefix(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.startswith("blurred-"):
                src = os.path.join(root, filename)
                new_name = os.path.join(root, filename.replace("blurred-", ""))
                os.rename(src, new_name)
                print(f"Renamed {filename} to {new_name}")

# Replace 'path_to_your_folder' with the path to your folder containing the images
folder_path = 'blured_photos_with_watermark'

remove_blurred_prefix(folder_path)