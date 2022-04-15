## script replaces /path/to string in file lahman_2016_import.sql
## with script folder path and csv subdirectory 

import os 
import sys

base_dir_path=os.path.dirname(os.path.abspath(__file__))

# print(base_dir_path)
new_path="/".join(base_dir_path.split("\\"))
old_path='/path/to'
file_name:str="/".join([new_path,"lahman_2016_import.sql"])
csv_name:str="/".join([new_path,"csv"])
try:
    with open(file_name) as in_file:
        text_py:str=in_file.read()
    new_text_py= text_py.replace(old_path,csv_name)
    # print(new_text_py)
    with open(file_name,"w") as out_file:
        out_file.write(new_text_py)
  
    print("Paths in", file_name , "were replaced")
except Exception as e:
    print("Error occurred")
    print("error: ",e)
    print("So, import script not ready to run.")
