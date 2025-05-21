
from addpairs import addpairs

from addition import addition

from checkEll import checkEll

from mult import mult


import math

def FindMult(AS,BS,G,orG,P,aE,bE,q):
    d = math.gcd(AS,orG)
    RorG = orG//d
    RAS = AS//d
    RBS = BS//d
    if BS%d != 0:
        print("No solution")
    else:
        xp = (pow(RAS,-1,RorG)*RBS)%orG
        j=0
        while j<orG:
           m=xp + j
           if P == mult(m,G,aE,bE,q):
               return m
           else:
               j=j+1
        return "error"
            
#w = FindMult(12,32,(70,61),40,(22,126),1,0,137)
#print(w)

