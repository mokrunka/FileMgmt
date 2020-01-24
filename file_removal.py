import os
from pathlib import Path

pathName = input("Type in the absolute pathname of the directory you want to remove: ")
dir_to_remove = Path(pathName)

#empty list of the timestamps each of the files in dir_to_remove
#example, the files are in the directory: R:\test\Test Dir for removal, input 'R:\test\Test Dir for removal' here
list_of_timestamps = []
file_counter = 0
with os.scandir(dir_to_remove) as dir_contents:
    for file in dir_contents:
        last_modified = file.stat()
        #go to internet and find the epoch timestamp for the date that you want to remove all files older than
        #1264040905 is 1/21/2010 at 2:28 AM GMT
        if last_modified.st_mtime <= 1579576600:
            list_of_timestamps.append(file)

#declare an empty filename to place-hold
full_file_name = ''

#this is going to remove some files
for file in list_of_timestamps:
    full_file_name = dir_to_remove / file
    os.remove(full_file_name)
    file_counter += 1

print("{file_counter} files were removed.")