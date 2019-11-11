"""This file is the main file. It's only purpose is to do some basic input checking, and to call the bcFindTarget function.
"""

#We import sys to hand the arguments given and to stop the program in case there is not enough
import sys
#We import our processing function from the bclib.py file
from bclib import bcFindTarget

sys.setrecursionlimit(10000)

#If the user doesn't use the program correctly we exit it 
if len(sys.argv) < 3 or len(sys.argv) > 4 :
    sys.exit("Usage : python3 blockchain.py <seed> <target_hash> [-p]")

#If it does, we start processing the input    
elif len(sys.argv) == 4 and sys.argv[3] == '-p' :
    bcFindTarget(str(sys.argv[1]), sys.argv[2], 0, True, '')
else:
    bcFindTarget(str(sys.argv[1]), sys.argv[2], 0, False, '')