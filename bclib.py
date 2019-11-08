import hashlib
import sys

global hasher
hasher = hashlib.md5()

def bcFindTarget(hash, target, iteration, printbool, stash):
    try:
        if printbool:
            print(str(iteration) + ' - ' + hash)

        if(hash != target):
            stash = str(hash)
            hasher.update(hash.encode("utf-8"))
            bcFindTarget(hasher.hexdigest(), target, iteration +1, printbool, stash)

        else:
            print("\nThe challenge hash " + target + " was found after " + str(iteration) + " iteration(s). Hurray !")
            print("It means that the string given to it was : " + stash)
            
    except:
        print('It looks like we could not find the hash you were looking for. Please note that Python\'s maximum iterations is 1000.')