import threading
import time
from check_duplicate_key import getKeys 
import difflib
import sys

def common_substrings(folder):
    keys = getKeys(folder)
    print(keys)
    substrings = []
    for i in range(len(keys[0])):
        for j in range(i + 1, len(keys[0]) + 1):
            substring = keys[0][i:j]
            all_contain_substring = True
            for k in range(1, len(keys)):
                if substring not in keys[k]:
                    all_contain_substring = False
                    break
            if all_contain_substring:
                substrings.append(substring)

    uniq_list(substrings)
    clean_list(substrings, 3)
    return substrings

def uniq_list(strings):
    use = 0
    for element in strings:
        a = 0
        for verif in strings:
            if a == 0:
                if element != verif:
                    if element in verif:
                        strings.remove(element)
                        use = use + 1
                        a = 1
    if use != 0:
        return uniq_list(strings)
    if use == 0:
        return 0

def clean_list(liste, size_limit):
    suppr = 0
    for element in liste:
        size = len(element)
        if (size <= size_limit):
            liste.remove(element)
            suppr = 1
    if suppr == 1:
        return clean_list(liste, size_limit)
    if suppr == 0:
        return 0


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        start = time.time()
        print(common_substrings(sys.argv[1])[1::][:-1])
        print("--- %s seconds ---" % (time.time() - start))
    else:
        print("Usage : python3 check_duplicate_key.py FOLDER")