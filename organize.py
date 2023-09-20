import os
import shutil

from_dir="C:/Users/Madhav Kumar Thakur/Downloads"
to_dir="C:/Users/Madhav Kumar Thakur/Documents"

list_of_files=os.listdir(from_dir)

print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)