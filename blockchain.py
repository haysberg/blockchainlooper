import sys
from bclib import bcFindTarget

seed = sys.argv[1]
target = sys.argv[2]
iteration = 0

bcFindTarget(seed, target, iteration)