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

alphabet = "abcdefghijklmnopqrstuvwxyz"
Nlet = 26
combs = list(itertools.combinations(alphabet, 2))
Ncombs = len(combs)

#print(Ncombs)

Score = np.zeros(Ncombs)

# Load in testing data
names = np.genfromtxt("Top200Names2010s.txt",dtype="U20")

words = np.genfromtxt("1000CommonWords.txt",dtype="U20")

#print(names)



for i in range(Ncombs):
    Nboth  = 0
    Nneith = 0
    for j in range(len(names)):
        l_let1 = False
        l_let2 = False
        for k in range(len(names[j])):
#            print(names[j][k].lower(),combs[i][0],names[k].lower() == combs[i][0])
            if names[j][k].lower() == combs[i][0]:
                l_let1 = True
            if names[j][k].lower() == combs[i][1]:
                l_let2 = True
        if l_let1 and l_let2:
            Nboth += 1
        else:
            Nneith += 1
    for j in range(len(words)):
        l_let1 = False
        l_let2 = False
        for k in range(len(words[j])):
            if words[j][k] == combs[i][0]:
                l_let1 = True
            if words[j][k] == combs[i][1]:
                l_let2 = True
        if l_let1 and l_let2:
            Nboth += 1
        else:
            Nneith += 1


    Score[i] = Nboth/(Nboth+Nneith)



combs = np.asarray(combs)

for i in range(Ncombs):
    print("{0} + {1} are in {2}% of names/words".format(combs[i,0],combs[i,1],Score[i]*100))

ind_Score = np.argsort(Score)
combs = combs[ind_Score]
Score = Score[ind_Score]


plt.hist(Score)
plt.savefig("DUMP.png")



# Get scores by letter
#ind_let = list(alphabet)

#ind_let_pair_score = np.empty((Nlet,1,Nlet),dtype=[('blet', 'U1'),('plet', 'U1'), ('score1', 'f8'),('score2', 'f8'),('score3', 'f8'),('score4', 'f8'),('score5', 'f8'),('score6', 'f8'),('score7', 'f8'),('score8', 'f8'),('score9', 'f8'),('score10', 'f8'),('score11', 'f8'),('score12', 'f8'),('score13', 'f8'),('score14', 'f8'),('score15', 'f8'),('score16', 'f8'),('score17', 'f8'),('score18', 'f8'),('score19', 'f8'),('score20', 'f8'),('score21', 'f8'),('score22', 'f8'),('score23', 'f8'),('score24', 'f8'),('score25', 'f8')])

ind_let_pair_score = np.zeros((Nlet,Nlet))
#ind_let_pair_score = [[0 for x in range(Nlet-1)] for y in range(Nlet)]

for i in range(Nlet):
    for j in range(Nlet):
        if i == j:
            ind_let_pair_score[i,j] = np.nan
        else:
            for k in range(len(Score)):
#                print(i, ord(combs[k,0])-97,j,ord(combs[k,1])-97)
                if ((i == ord(combs[k,0])-97 and j == ord(combs[k,1])-97) or 
                   (i == ord(combs[k,1])-97 and j == ord(combs[k,0])-97)):
#                    print(chr(i+97),chr(j+97),combs[k,0],combs[k,1])
#                    print("in")
                    ind_let_pair_score[i][j] = Score[k]
                    break



# For each letter find the minimum value for a pair,
# then take the maximum(???) value from that list

pairs    = np.empty((Nlet//2,2),dtype="U1")
ind_mins = np.zeros(Nlet,dtype=int)
sc_mins  = np.zeros(Nlet)



for n in range(Nlet//2):
    ind_mins[:] = 0
    sc_mins[:]  = 0. 

    # Find the minimum score for each letter
    for i in range(len(ind_let_pair_score)):
        if not np.all(np.isnan(ind_let_pair_score[i,:])):
            ind_mins[i] = np.nanargmin(ind_let_pair_score[i])
            sc_mins[i]  = np.nanmin(ind_let_pair_score[i])
        else:
#            print(i,ind_let_pair_score[i,:])
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

print("Scorecard!")
print("My simple algorithm can spell {0:5.2f}% of the words and names".format(Nspell/(Nspell+NNospell)*100))


block_pairs = np.array([['f','s'],['b','o'],['j','w'],['z','m'],['v','e'],['r','a'],['n','i'],
                        ['d','q'],['h','u'],['l','y'],['p','c'],['t','g'],['x','k']],dtype='U1')


Nspell   = 0
NNospell = 0
for name in names:
    lcanspell = True
    for pair in block_pairs:
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
        Nspell += 1
    else:
        NNospell += 1
for word in words:
    lcanspell = True
    for pair in block_pairs:
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


print("The blocks as constructed can spell {0:5.2f}% of the words and names".format(Nspell/(Nspell+NNospell)*100))





















