__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
from urllib.parse import parse_qsl
import zipfile
#import readlines

from black import Line

current_dir = os.getcwd()
files_dir = os.path.join(current_dir, 'files')
cache = os.path.join(files_dir, 'cache')


# Create a new empty Cache folder
def clean_cache():
    if os.path.exists(cache):
        shutil.rmtree(cache)    
    os.makedirs(cache)

# Unzip all files to cache dir  
def cache_zip(file_path, cache_dir):
    if os.path.exists(cache_dir):
        clean_cache()
    with zipfile.ZipFile(file_path, 'r') as zip:
        zip.extractall(cache_dir)

# List all files in the cache folder
def cached_files():
    abs_file_path = []
    for i in os.listdir(cache):
        k = os.path.abspath(os.path.join(cache, i))
        abs_file_path.append(k)
    return abs_file_path

def find_password(cached_files):
    for i in cached_files:
        with open(i) as pass_file:
            pass_line = pass_file.readlines()
            for line in pass_line:
                if 'password' in line:
                    found_pass = line 
                    pass_file.close()
                    break
                else:
                    continue
    return found_pass[10::].rstrip()    
        

#clean_cache()
#cache_zip(r'c:/Users/Homer/PythonProjects/Winc/files/data.zip', r'c:/Users/Homer/PythonProjects/Winc/files/cache/')
#print(cached_files())
print(find_password(cached_files()))