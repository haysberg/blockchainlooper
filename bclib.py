import hashlib
import sys

global hasher, printer
hasher = hashlib.md5()
printer = "0"

if len(sys.argv) > 3 :
    printer = sys.argv[3]

def bcFindTarget(hash, target, iteration):
    if printer == "1":
        print(hash)

    if(hash == target):
        print("The target " + target + " was found after " + str(iteration) + " iterations. Hurray !")
    else:
        hasher.update(hash.encode("utf-8"))
        bcFindTarget(hasher.hexdigest(), target, iteration +1)