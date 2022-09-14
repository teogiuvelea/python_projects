# import OS module
import os
 
# Get the list of all files and directories
path = "img_dir/"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(dir_list)
for item in dir_list:
    with open("pics_title.txt", "a") as f:
        f.write(item + "\n")