import subprocess
import sys
import difflib
import os
import time

def getKeys(folder):
    keys = []
    for file in os.listdir(folder):
        key = open(folder+"/"+file,"rb").read()
        keys.append(key)
        
    return keys

def check_duplicate(folder):
    keys = getKeys(folder)
    unique = set(keys)
    if len(keys) == len(unique):
        print("No duplicate")
    else:
        print("There is : %s duplicate" % len(keys) - len-unique)


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        start = time.time()
        check_duplicate(sys.argv[1])
        print("--- %s seconds ---" % (time.time() - start))
    else:
        print("Usage : python3 check_duplicate_key.py FOLDER")