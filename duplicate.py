import os, sys

import hashlib

BLOCK_SIZE = 65536







def get_file_hash(file_name, dir):
    file_path = os.path.join(dir, file_name)
    file = open(file_path, 'rb')
    hasher = hashlib.md5()
    block_file = file.read(BLOCK_SIZE)
    while len(block_file) > 0:
        hasher.update(block_file)
        block_file = file.read(BLOCK_SIZE)
    file.close()
    return hasher.hexdigest()
def find_duplicate_files(dir_path):
    hash_dict = {}
    filenames = []
    for dir, subdir, files in os.walk(dir_path):
         filenames = files
    for file in filenames:
         file_hash = get_file_hash(file, dir_path)
         if hash_dict.get(file_hash):
            hash_dict[file_hash].append(file)
         else:
            hash_dict[file_hash] = [file]
    for key, value in hash_dict.items():
         if len(value) > 1:
             print(value)
if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 1:
          print("Multiple Directories are given.")
    elif len(args) == 0:
          print("No Directory is given")
    elif os.path.exists(args[0]):
          find_duplicate_files(args[0])
    else:
        print("No such Directory Exists")
