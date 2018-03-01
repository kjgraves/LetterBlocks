#!/usr/bin/env python3.5
# WordCombinations.py
#
# Author: Kevin Graves
# Last Modified: Feb 28, 2018
# Description: Calculate the number of ways that 26 letters can be paired off
# 
# Notes: 
################################################################################

import numpy as np
import math


# This is how i think of the problem, 
#       later I found a solution posted stackexchange which got the same solution
# Simple algorithm to calculate the number of ways to pair off 2*"i" pairs
# For two letters, there is only one choice
# For four letters (i = 2), there are 3 choices
#   One way to think of it:
#      pair1    pair2
#       a+b      c+d
#   Then a can stay put and you can cycle, b, c, and d to the right (or left)
#   until they reach their starting point, and each one will generate a new set of pairs
# For six letters:
#       pair1   pair2   pair3
#        a+b     c+d     e+f
#   you can generate the same number of pairings with just pair2 and pair3 as in four 
#   letters, but a can be paired with 5 (6-1 or 2*i-1) different letters and each pairing
#   with a will give 3 more pairings
# In general:
#   You can generate the same number of pairings with i-1 pairs. By adding another pair, adds
#   one less than the number of letters (2*i-1) way to create a single pair, each of which will have
#   the same number of pairings as with i-1 pairs.
# Soooo.... 
#
N = 1
i = 1
print("Number of combinations for {0} letters = {1}".format(2*i,N))
for i in range(2,14):
    N = (2*i - 1)*N
    print("Number of combinations for {0} letters = {1}".format(2*i,N))

Ntotpairings = N

# Ok probably the "better," discrete mathematically inclined way to do this:
# Directly snaged from: https://math.stackexchange.com/questions/532542/there-are-10-different-people-at-a-party-how-many-ways-are-there-to-pair-them-o
N = int(math.factorial(26)/(2**13 * math.factorial(13)))
print("Other algorithm finds {0} combinations for {1} letters".format(N,26))












