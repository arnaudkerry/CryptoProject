import sys
from cryptography.hazmat.primitives import serialization


def check_duplicate(file):
    with open(file, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None
        )
        print(private_key)
    return

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        check_duplicate(sys.argv[1])
    else:
        print("Usage : python3 check_duplicate_key.py FILE")