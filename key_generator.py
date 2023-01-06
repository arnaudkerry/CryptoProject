from OpenSSL.crypto import PKey
from OpenSSL.crypto import TYPE_RSA
from OpenSSL.crypto import dump_publickey
from OpenSSL.crypto import FILETYPE_PEM
import sys

def gen_key(bits: int = 512):
    key = PKey()
    key.generate_key(TYPE_RSA,bits)
    return dump_publickey(FILETYPE_PEM,key)

def generate(nb, bits = 512):
    f = open("keyfile.txt", "ab+")
    for i in range(int(nb)):
        f.write(gen_key(bits))

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("Usage : key_generator n [bits]")
    if(len(sys.argv) == 2):
        generate(int(sys.argv[1]))
    if(len(sys.argv) == 3):
        generate(int(sys.argv[1]), int(sys.argv[2]))