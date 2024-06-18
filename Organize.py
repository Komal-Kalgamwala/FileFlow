import os
import shutil

def organize_files(source_dir, destination_dir):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            file_extension = os.path.splitext(filename)[1]
            file_extension = file_extension.lower()

            if file_extension:
                destination_subdir = os.path.join(destination_dir, file_extension[1:])
                if not os.path.exists(destination_subdir):
                    os.makedirs(destination_subdir)

                destination_path = os.path.join(destination_subdir, filename)
                shutil.move(source_path, destination_path)
                print(f"Moved '{filename}' to '{destination_subdir}'")

if __name__ == "__main__":
    source_directory = r"C:\Users\kkalg\OneDrive\Desktop\Komal Kalgamwala\Source"  # Replace with the source directory path
    destination_directory = r"C:\Users\kkalg\OneDrive\Desktop\Komal Kalgamwala\Destination"  # Replace with the destination directory path
    
    organize_files(source_directory, destination_directory)
