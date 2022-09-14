# import OS module
import os
 
# Get the list of all files and directories
def directory_items(directory):
    # directory = 'video_files'
    # directory = 'audio_files'
    path = directory
    dir_list = os.listdir(path)
    
    print("Listing and saving all files from", directory)
    
    # prints all files
    print(dir_list)
    for item in dir_list:
        with open(f"{directory}.txt", "a") as f:
            f.write(item + "\n")