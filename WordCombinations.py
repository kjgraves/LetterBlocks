#!/usr/bin/env python3.5
# WordCombinations.py
#
# Author: Kevin Graves
# Last Modified: Feb 9, 2018
# Description: Find the best combination of word blocks
# 
# Notes: 
################################################################################

import numpy as np
import itertools

# Number of combinations 
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


print("There are {0} ways to combine the letter into pairs to print on blocks".format(choose(26,13)))
print("no")

N = 1
i = 1
print("Number of combinations for {0} pair = {1}".format(i,N))
for i in range(2,14):
    N = (2*i - 1)*N
    print("Number of combinations for {0} pair = {1}".format(i,N))

Ntotpairings = N
print(Ntotpairings)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
aPairs = ["AB","CD","EF","GH","IJ","KL","MN","OP","QR","ST","UV","WX","YZ"]
NPairs = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[23,24],[25,26]])
NPairs = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])

NPair_now = NPairs
print(NPair_now[-6:])
Ntimes = 10
level = 2 # 
rot = 1
for i in range(14):
    print(rot,level,rot*2 - 1)
    if level*2 - 1 == rot:
        level += 1
        rot = 0
#        print(2222)
        NPair_now = NPairs

    tmp = np.array(NPair_now[-2*level+1:])
    for j in range(1,2*level):
        if j == 1:
            NPair_now[-j] = tmp[0]
        else:
            NPair_now[-j] = tmp[-j+1]
    rot += 1
    print(NPair_now[-6:])
#def combinations(iterable, r):
#    # combinations('ABCD', 2) --> AB AC AD BC BD CD
#    # combinations(range(4), 3) --> 012 013 023 123
#    pool = tuple(iterable)
#    n = len(pool)
#    if r > n:
#        return
#    indices = range(r)
#    yield tuple(pool[i] for i in indices)
#    while True:
#        for i in reversed(range(r)):
#            if indices[i] != i + n - r:
#                break
#        else:
#            return
#        indices[i] += 1
#        for j in range(i+1, r):
#            indices[j] = indices[j-1] + 1
#        yield tuple(pool[i] for i in indices)

##alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
##res = itertools.combinations(alphabet,13)
##for result in res:
##    print(result)
#NPairs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#def all_pairs(lst):
#    if len(lst) < 2:
#        yield lst
#        return
#    a = lst[0]
#    for i in range(1,len(lst)):
#        pair = (a,lst[i])
#        for rest in all_pairs(lst[1:i]+lst[i+1:]):
#            yield [pair] + rest

#n = 1
#for x in all_pairs(NPairs):
#    print("{0}".format(n/Ntotpairings))
#    n += 1












