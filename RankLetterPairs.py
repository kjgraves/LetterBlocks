#!/usr/bin/env python3.5
# RankLetterPairs.py
#
# Author: Kevin Graves
# Last Modified: Feb 9, 2018
# Description: Rank the letter pairings
# 
# Notes: 
################################################################################

import numpy as np
import itertools
import matplotlib.pyplot as plt 

# FUNCTIONS
def double_letters(word):
    """
    Simple function to test for duplicated letters in a word.
    INPUT: word - a string of charaters
    OUTPUT: True - if there are any duplicated letters
            False - if there are no duplicated letters
    """
    retval = False
    for i in range(len(word)-1):
        for j in range(i+1,len(word)):
            if word[i] == word[j]:
                retval = True
                break
    return retval

# Main Program

alphabet = "abcdefghijklmnopqrstuvwxyz"
Nlet = 26

# Find all of the combinations of the the letters
combs = np.array(list(itertools.combinations(alphabet, 2)))
Ncombs = len(combs)

print("There are {0} different combinations from 26 letters".format(Ncombs))

# Load in testing data
names = np.genfromtxt("Top200Names2010s.txt",dtype="U20")
words = np.genfromtxt("1000CommonWords.txt",dtype="U20")

# Remove any double letters because the letter blocks can never spell them
ind_dl = np.where([not double_letters(name) for name in names])
names = names[ind_dl]
ind_dl = np.where([not double_letters(word) for word in words])
words    = words[ind_dl]

# Initialize variable to hold score for each letter combination
Score = np.zeros(Ncombs)

# Loop to test if both letters are in each name/word 
# The score is the percentage of names/words that have both letters
for i in range(Ncombs):
    Nboth  = 0
    Nneith = 0
    for j in range(len(names)):
        l_let1 = False
        l_let2 = False
        for k in range(len(names[j])):
#            print(names[j][k].lower(),combs[i,0],names[k].lower() == combs[i,0])
            if names[j][k].lower() == combs[i,0]:
                l_let1 = True
            if names[j][k].lower() == combs[i,1]:
                l_let2 = True
        if l_let1 and l_let2:
            Nboth += 1
        else:
            Nneith += 1
    for j in range(len(words)):
        l_let1 = False
        l_let2 = False
        for k in range(len(words[j])):
            if words[j][k] == combs[i,0]:
                l_let1 = True
            if words[j][k] == combs[i,1]:
                l_let2 = True
        if l_let1 and l_let2:
            Nboth += 1
        else:
            Nneith += 1


    Score[i] = Nboth/(Nboth+Nneith)


for i in range(Ncombs):
    print("{0} + {1} are in {2}% of names/words".format(combs[i,0],combs[i,1],Score[i]*100))

# Sort by the Score
ind_Score = np.argsort(Score)
combs = combs[ind_Score]
Score = Score[ind_Score]


plt.hist(Score*100,edgecolor='k',normed=True,bins=20)
plt.xlabel("Percentage of words containing both letters")
plt.ylabel("Number of Pairs")
plt.xlim(0,25)
plt.savefig("AllPairScore.png")
plt.clf()

ind_e = np.where((combs[:,0] == 'e') | (combs[:,1] == 'e'))

plt.hist(Score[ind_e]*100,edgecolor='k',normed=True)
plt.xlabel("Percentage of words containing \"e\" and another letter")
plt.ylabel("Number of Pairs")
plt.xlim(0,25)
plt.savefig("EPairScore.png")
plt.clf()

ind_q = np.where((combs[:,0] == 'q') | (combs[:,1] == 'q'))

plt.hist(Score[ind_e]*100,edgecolor='k',normed=True)
plt.xlabel("Percentage of words containing \"q\" and another letter")
plt.ylabel("Number of Pairs")
plt.xlim(0,25)
plt.savefig("QPairScore.png")
plt.clf()


# Get scores by each letter
ind_let_pair_score = np.zeros((Nlet,Nlet))
# Note: The diagonals of this 2D array don't mean anything (and we will set them to NaN)

for i in range(Nlet):
    for j in range(Nlet):
        if i == j:
            ind_let_pair_score[i,j] = np.nan
        else:
            for k in range(len(Score)):
                if ((i == ord(combs[k,0])-97 and j == ord(combs[k,1])-97) or 
                   (i == ord(combs[k,1])-97 and j == ord(combs[k,0])-97)):
                    ind_let_pair_score[i][j] = Score[k]
                    break

# Before we jump into the actual alorithm for calulating a good way 
#   to pair the letter blocks, lets first find out:
#   2) How the letter blocks score as they are

# How the letter blocks score as they are
# Here are the pairings
block_pairs = np.array([['f','s'],['b','o'],['j','w'],['z','m'],['v','e'],['r','a'],['n','i'],
                        ['d','q'],['h','u'],['l','y'],['p','c'],['t','g'],['x','k']],dtype='U1')

# Find all of the words that can be spelled with this grouping of pairs
Nspell   = 0
NNospell = 0
for name in names:
    lcanspell = True
    for pair in block_pairs:
        l_let1 = False
        l_let2 = False
        for let in name:
            if let.lower() == pair[0]:
                l_let1 = True
            elif let.lower() == pair[1]:
                l_let2 = True
        if l_let1 and l_let2:
            lcanspell = False
            break
    if lcanspell:
        Nspell += 1
    else:
        NNospell += 1
for word in words:
    lcanspell = True
    for pair in block_pairs:
        l_let1 = False
        l_let2 = False
        for let in word:
            if let.lower() == pair[0]:
                l_let1 = True
            elif let.lower() == pair[1]:
                l_let2 = True
        if l_let1 and l_let2:
            lcanspell = False
            break
    if lcanspell:
        Nspell += 1
    else:
        NNospell += 1

print("Scorecard!")
print("The blocks as constructed can spell {0:5.2f}% of the words and names".format(Nspell/(Nspell+NNospell)*100))


# Actual Algorithm Part!

# First Intialize Arrays
pairs    = np.empty((Nlet//2,2),dtype="U1")
ind_mins = np.zeros(Nlet,dtype=int)
sc_mins  = np.zeros(Nlet)

# MY SIMPLE ALGORITHM
# For each letter find the minimum Score for all pairs,
# then take the MAXIMUM value from those scores

for n in range(Nlet//2):
    ind_mins[:] = 0
    sc_mins[:]  = 0. 

    # Find the minimum score for each letter
    for i in range(len(ind_let_pair_score)):
        if not np.all(np.isnan(ind_let_pair_score[i,:])):
            ind_mins[i] = np.nanargmin(ind_let_pair_score[i])
            sc_mins[i]  = np.nanmin(ind_let_pair_score[i])
        else:
            ind_mins[i] = 99 # Should never choose this
            sc_mins[i]  = np.nan

    # Choose the score with the biggest
    choice_ind = np.nanargmax(sc_mins)
    pair_ind   = ind_mins[choice_ind]

    # Save the pair and make all rows and cols of those letters nan
    pairs[n,0] = chr(choice_ind+97)
    pairs[n,1] = chr(pair_ind+97)
    ind_let_pair_score[choice_ind,:] = np.nan
    ind_let_pair_score[:,choice_ind] = np.nan
    ind_let_pair_score[pair_ind,:] = np.nan
    ind_let_pair_score[:,pair_ind] = np.nan



print("Best Pairs:")
for i in range(Nlet//2):
    print("{0} + {1}".format(pairs[i,0],pairs[i,1]))   

# Score?
Nspell   = 0
NNospell = 0
for name in names:
    lcanspell = True
    for pair in pairs:
        l_let1 = False
        l_let2 = False
        for let in name:
#            print(names[j][k].lower(),combs[i][0],names[k].lower() == combs[i][0])
            if let.lower() == pair[0]:
                l_let1 = True
            elif let.lower() == pair[1]:
                l_let2 = True
        if l_let1 and l_let2:
            lcanspell = False
            break
    if lcanspell:
#        print("'{0}',".format(name))
        Nspell += 1
    else:
        NNospell += 1
for word in words:
    lcanspell = True
    for pair in pairs:
        l_let1 = False
        l_let2 = False
        for let in word:
#            print(names[j][k].lower(),combs[i][0],names[k].lower() == combs[i][0])
            if let.lower() == pair[0]:
                l_let1 = True
            elif let.lower() == pair[1]:
                l_let2 = True
        if l_let1 and l_let2:
            lcanspell = False
            break
    if lcanspell:
        Nspell += 1
    else:
        NNospell += 1

print("My simple algorithm can spell {0:5.2f}% of the words and names".format(Nspell/(Nspell+NNospell)*100))






















