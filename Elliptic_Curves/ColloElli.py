# Collision attack elliptic curve 

''' Input:
           Elliptic curve y^2 = x^3 + aEx + bE  (mod p)
           aE, bE are decimal integers
           
           p is hexa string 
           Generator G coordinates Gx, Gy 
           Point P coordinates xS,yS 

           orG = order of generator G  in decimal

    Output: m integer such that
            mG = P  on the input elliptic curve
            

'''

from addpairs import addpairs

from addition import addition

from checkEll import checkEll

from multB import multB

import os
import math

from FindMult import FindMult


# Input

aE = 1   # aE integer decimal
bE = 7    # bE  integer decimal


G=(7,9)
orG = 18  # orG integer decimal
q=23
p='{:x}'.format(q)

P=(4,12)


Xcoord = open('Xcoord.txt','w')
RNDpairs = open('RNDpairs.txt','w')
Solution = open('Solution.txt','w')

##########################################

ran = math.ceil(len(p)/2)
lam = len(p)*4
 



ct=0

print("Go !")
pairs=[]
lista=[]
pt=q
j=0
flag = True
while j < pt and flag:
    ct = ct + 1
    v=os.urandom(ran)
    w='0x'+v.hex()
    number, pad, rjust, size, kind = int(w, 16), '0', '>', lam, 'b'
    a=f'{number:{pad}{rjust}{size}{kind}}'
    v=os.urandom(ran)
    w='0x'+v.hex()
    number, pad, rjust, size, kind = int(w, 16), '0', '>', lam, 'b'
    b=f'{number:{pad}{rjust}{size}{kind}}'
    AA = multB(a,G,aE,bE,q)
    BB = multB(b,P,aE,bE,q)
    m = addition(AA,BB,aE,bE,q)
    if m == "O" or m[0] in lista:
        print("Collission!")
        if m == "O":
            print(a," *G + ",b," *P = O")
            AS = -int(a,2)
            BS = int(b,2)
            sk = FindMult(BS,AS,G,orG,P,aE,bE,q)
            Solution.write(str(sk%orG))
            flag = False
        else:
             dove = lista.index(m[0])
             A = pairs[dove][0]
             B = pairs[dove][1]
             Aw = multB(A,G,aE,bE,q)
             Bw = multB(B,P,aE,bE,q)
             if addition(Aw,Bw,aE,bE,q) == m:
                 print(int(a,2)%orG,"G +",int(b,2)%orG,"P = ",int(A,2)%orG,"G + ",int(B,2)%orG,"P")
                 AS = (int(B,2)-int(b,2))%orG
                 BS = (int(a,2)-int(A,2))%orG
                 #print("solve ",AS,"x =",BS)
                 sk = FindMult(AS,BS,G,orG,P,aE,bE,q)
                 Solution.write(str(sk%orG))
             else:
                 AS = (int(B,2)+int(b,2))%orG
                 BS = (-int(a,2)-int(A,2))%orG
                 #print("solve ",AS,"x =",BS)
                 sk = FindMult(AS,BS,G,orG,P,aE,bE,q)
                 Solution.write(str(sk%orG))
             flag = False
    else:
        lista.append(m[0])
        Xcoord.write(str(m[0])+",")
        pairs.append((a,b))
        RNDpairs.write(a+","+b+"|")
    j=j+1
    if j%1000==0: print(j,len(lista),len(pairs))
print(ct, "  birthday")

Xcoord.close()
RNDpairs.close()
Solution.close()
print(sk%orG)
print("The End")
