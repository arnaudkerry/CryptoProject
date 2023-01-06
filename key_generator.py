from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import sys

def gen_key(bits: int = 512):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits
    )
    return private_key.private_bytes(encoding=Encoding.PEM,format=PrivateFormat.TraditionalOpenSSL,encryption_algorithm=NoEncryption())

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