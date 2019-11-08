import sys
from bclib import bcFindTarget

seed = sys.argv[1]
target = sys.argv[2]
iteration = 0

bcFindTarget(str(seed.encode('utf-8')), target, iteration)