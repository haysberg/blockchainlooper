"""This file contains the processing function that allows us to find the hash challenge
"""

#We import hashlib for the md5 hashes
import hashlib

#We declare a global variable, allowing us to make our code shorter
global hasher
hasher = hashlib.md5()


def bcFindTarget(hash, target, iteration, printbool, stash):
    """This is the main processing function to find the challenge hash.
    
    Arguments:
        hash {string} -- The string that will be hashed later, and compared to the target hash
        target {string} -- The hash that we are trying to find
        iteration {integer} -- This counts how many times the function has been called. If we find the hash just after the seed, it'll be equal to 1.
        printbool {boolean} -- If this boolean equals true, we will print the intermediate hashes. Enable it using -p at the end of the command
        stash {string} -- This variable contains the previous hash that we found. If the hash of this string is equal to our target, we display it as well.
    """
    try:
        #If the printing option is enabled, we display the intermediate hash that we calculated
        if printbool:
            print(str(iteration) + ' - ' + hash)

        #If the hash is not equal to our target, we continue processing the hash using recursive programming
        if(hash != target):
            #We store the previous hash in the stash in case that we find the matching hash next iteration
            stash = str(hash)

            #We then hash the current 'hash' variable and feed it to this function again
            hasher.update(hash.encode("utf-8"))
            bcFindTarget(hasher.hexdigest(), target, iteration +1, printbool, stash)

        #If the hash equals the target, we print this message to inform the user that we found it, and display the hash given in input as well.
        else:
            print("\nThe challenge hash " + target + " was found after " + str(iteration) + " iteration(s). Hurray !")
            print("It means that the string given to it was : " + stash)
            
    #If we run into an exception, we display this message. Usually, an exception is raised when we iterate more than 1000 on the same function.
    #But this also covers other exception.
    except:
        print('It looks like we could not find the hash you were looking for. Please note that Python\'s maximum iterations is 1000.')