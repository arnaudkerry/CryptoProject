import subprocess
import threading
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import sys
import os
import time


def storeKeys(file):
    f = open(file, "rb")
    f.readline().decode("utf-8").split()
    return f.read().split(b"-----END RSA PRIVATE KEY-----\n")
    
def compare(a,b):
    if a == b:
        print("Found ! : %s" % a)
        return -1

def floydAlgorithm(f,key,a0):
    m = 1
    tortue = f(a0,key)
    lievre = f(f(a0,key),key)

    while tortue != lievre:
        m = m + 1
        tortue = f(tortue,key)
        lievre = f(f(lievre,key),key)
    
    return m

def next(nb,keys):
    print(nb)
    return keys[nb+1]
    

def format_Text(file):
    subprocess.call(["sed '/^-----BEGIN RSA PRIVATE KEY-----/d' %s > out.txt" % file], shell=True)
    start = time.time()    
    keys = storeKeys("out.txt")
    for a in keys:
        print("%s\n----\n" % a)
    floydAlgorithm(next,keys[0],0)
    print("--- %s seconds ---" % (time.time() - start))
    #subprocess.call(["rm out.txt"], shell=True)


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        format_Text(sys.argv[1])
    else:
        print("Usage : python3 floyd_algorithm.py FILE")