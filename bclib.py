import hashlib

def bcFindTarget(hash, target, iteration):
    print(hash)
    if(hash == target):
        print("The target " + target + " was found after " + str(iteration) + " iterations. Hurray !")
    else:
        m = hashlib.md5()
        m.update(hash.encode("utf-8"))
        bcFindTarget(m.hexdigest(), target, iteration +1)