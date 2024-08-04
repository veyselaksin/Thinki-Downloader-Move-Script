# Description: This script for the move child files to parent directory
import os


def move_files_to_parent_directory(directory: str):
    # Get the list of files in the current directory
    files = os.listdir(directory)
    # Loop through the files
    for file in files:
        app_dir = os.path.join(directory, file)
        # Check if the file is a directory
        if os.path.isdir(app_dir):
            # Get the list of files in the directory
            child_files = os.listdir(app_dir)
            # Loop through the child files
            for child_file in child_files:
                # Move the child file to the parent directory
                # if the file is not a directory continue
                if not os.path.isdir(os.path.join(app_dir, child_file)):
                    continue
                files = os.listdir(os.path.join(app_dir, child_file))
                for f in files:
                    os.rename(os.path.join(app_dir, child_file, f), os.path.join(app_dir, f))
                # Remove the directory
                os.rmdir(os.path.join(app_dir, child_file))


if __name__ == '__main__':
    move_files_to_parent_directory("./amazon-pro-club")
