# this clean script is used to clean the git repo for mac, because mac will generate some temporary files, such as .DS_Store,
# Thumbs.db, and some temporary files with suffix .tmp, .bak, .log, and some temporary folders with name tmp, output, outputs. These files and folders are not needed in the git repo, so we can use this script to clean them.
# Note: this script will delete the files and folders permanently, and it will use git command to remove the files and folders from the git repo, so please make sure you have committed all your changes before running this script.

# !!! Please make sure you have committed all your changes before running this script!!!
import os
import subprocess
temp_files = ["*.tmp", "*.bak", "*.log", ".DS_Store", "Thumbs.db"]
temp_folders = ["tmp", "output", "outputs"]

def recursive_delete(folder):
    for root, dirs, files in os.walk(folder):
        print(f"Checking folder: {root}, find dirs: {dirs}, find files: {files}")
        for file in files:
            if file.endswith(".tmp") or file.endswith(".bak") or file.endswith(".log") or file == ".DS_Store" or file == "Thumbs.db":
                file_path = os.path.join(root, file)
                subprocess.run(["git", "rm", "-rf", file_path], check=True)
        for dir in dirs:
            if dir == "tmp" or dir == "output" or dir == "outputs":
                dir_path = os.path.join(root, dir)
                subprocess.run(["git", "rm", "-rf", dir_path], check=True)

if __name__ == "__main__":
    # define the temporary files and folders to be deleted
    # recursively delete the temporary files and folders
    recursive_delete(".")

    print("Cleaned the git repo successfully!")