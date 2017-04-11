import math
import random

def createRandomPairs(size, shuffle=random.shuffle):
    x=range(size)
    y=range(size)
    shuffle(x)
    shuffle(y)
    for i in x:
        for j in y:
            yield (i,j)

def pathCombinations(path):
    for i,j in createRandomPairs(len(path)):
        if i < j:
            copy=path[:]
            copy[i],copy[j]=path[j],path[i]
            yield copy

listnew = createRandomPairs(20)
