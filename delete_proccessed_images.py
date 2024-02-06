import os

source_folder = "data/photo"
output_folder = "unblured_photos"

def delete_matching_files(source_folder, output_folder):
    # Get list of files in output folder
    output_files = os.listdir(output_folder)

    # Iterate over each file in the output folder
    for file_name in output_files:
        # Check if the file is an image
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Check if the file exists in the source folder
            source_file_path = os.path.join(source_folder, file_name)
            if os.path.exists(source_file_path):
                # Delete the file from the source folder
                os.remove(source_file_path)
                print(f"Deleted {file_name} from {source_folder}")

# Call the function
delete_matching_files(source_folder, output_folder)
