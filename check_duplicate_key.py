import subprocess
import sys
import itertools
import threading
import time

def check_duplicate(file):
    f = open(file, "rb")
    infos = f.readline().decode("utf-8").split()
    nbKey = int(infos[0])
    keys = f.read().split(b"-----END RSA PRIVATE KEY-----")
    for a,b in itertools.combinations(keys, 2):
        threading.Thread(target=compare,args=(a,b)).start()

def compare(a,b):
    if a == b:
        print("Found ! : %s" % a)
        return -1
    

def format_Text(file):
    subprocess.call(["sed '/^-----BEGIN RSA PRIVATE KEY-----/d' %s > out.txt" % file], shell=True)
    start = time.time()    
    check_duplicate("out.txt")
    print("--- %s seconds ---" % (time.time() - start))
    subprocess.call(["rm out.txt"], shell=True)


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        format_Text(sys.argv[1])
    else:
        print("Usage : python3 check_duplicate_key.py FILE")