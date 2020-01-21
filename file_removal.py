import os
from pathlib import Path

pathName = input("Type in the absolute pathname of the directory you want to remove: ")
dir_to_remove = Path(pathName)

#empty list of the timestamps each of the files in dir_to_remove
list_of_timestamps = []

with os.scandir(dir_to_remove) as dir_contents:
    for file in dir_contents:
        last_modified = file.stat()
        #go to internet and find the epoch timestamp for the date that you want to remove all files older than
        if last_modified.st_mtime <= 1579574184:
            list_of_timestamps.append(file)

#declare an empty filename to place-hold
full_file_name = ''

#this is going to remove some files
for file in list_of_timestamps:
    full_file_name = dir_to_remove / file
    os.remove(full_file_name)