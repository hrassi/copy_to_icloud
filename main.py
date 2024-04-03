import os
import shutil

####### reading from the file file_path.txt the file path
######  and store it in a variable called : path_from_file
def read_path_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            path = file.read().strip()  # Read the path and remove any leading/trailing whitespace
            return path
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

if __name__ == "__main__":
    # Assuming the text file is named "path_file.txt" and located in the same directory as the script
    path_file_path = "file_path.txt"

    # Read the path from the file
    path_from_file = read_path_from_file(path_file_path)

    if path_from_file:
        print("Path read from file:", path_from_file)
        # Now you can use the 'path_from_file' variable as needed in your script
    else:
        print("Unable to read path from file.")


###### get the icloud drive path
#####  and store it in a variable called : icloud_drive_path
def get_icloud_drive_path():
    # Expand the user's home directory and append the iCloud Drive path
    icloud_drive_path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs")

    if os.path.exists(icloud_drive_path):
        return icloud_drive_path
    else:
        print("iCloud Drive path does not exist.")
        return None


if __name__ == "__main__":
    icloud_drive_path = get_icloud_drive_path()
    if icloud_drive_path:
        print("iCloud Drive Path:", icloud_drive_path)



icloud_destination = icloud_drive_path
source_file = path_from_file

print('Source File Path :',source_file)


####### copy file from source location on hd to icloud drive
def copy_to_icloud(source_file, icloud_destination):
    try:
        # Copy the file from the source location to the iCloud Drive destination
        shutil.copy2(source_file, icloud_destination)
        print("File copied successfully to iCloud Drive.")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied to copy the file.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":

    copy_to_icloud(source_file, icloud_destination)
