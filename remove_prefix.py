import os

def remove_blurred_prefix(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.startswith("изображение_"):
                src = os.path.join(root, filename)
                new_name = os.path.join(root, filename.replace("изображение_", ""))
                os.rename(src, new_name)
            if filename.startswith("зображення_"):
                src = os.path.join(root, filename)
                new_name = os.path.join(root, filename.replace("зображення_", ""))
                os.rename(src, new_name)
            

# Replace 'path_to_your_folder' with the path to your folder containing the images
folder_path = 'data/photo'

remove_blurred_prefix(folder_path)