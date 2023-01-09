import threading
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import sys
import os
import time

def gen_key(bufferFile,bits: int = 512):
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits
    )
    bufferFile.write(private_key.private_bytes(encoding=Encoding.PEM,format=PrivateFormat.TraditionalOpenSSL,encryption_algorithm=NoEncryption()))

def generate(nb, bits = "512"):
    if os.path.exists("keyfile.txt"):
        os.remove("keyfile.txt")
    f = open("keyfile.txt", "ab+")
    line = nb+" \n"
    f.write(bytes(line, "utf-8"))
    for i in range(int(nb)):
        threading.Thread(target=gen_key,args=(f,int(bits))).start()
        

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("Usage : key_generator n [bits]")
    if(len(sys.argv) == 2):
        start = time.time()
        generate(sys.argv[1])
        print("--- %s seconds ---" % (time.time() - start))
    if(len(sys.argv) == 3):
        generate(sys.argv[1], int(sys.argv[2]))