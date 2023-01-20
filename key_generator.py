import subprocess
import sys
import time

def gen(nb, bits = 512):
    subprocess.call(["rm -rf keys"], shell=True)
    subprocess.call(["bash key_gen.sh %s %s" % (nb,bits)], shell=True)
        

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("Usage : key_generator n [bits]")
    if(len(sys.argv) == 2):
        start = time.time()
        gen(int(sys.argv[1]))
        print("--- %s seconds ---" % (time.time() - start))
    if(len(sys.argv) == 3):
        gen(sys.argv[1], int(sys.argv[2]))