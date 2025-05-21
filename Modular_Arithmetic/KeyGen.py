from random import randrange

from SqM import squaremultiply

def KeyGen(p,g):
    sk = randrange(p)   # from 0 to p-1 inclusive
    pk = squaremultiply(g,sk,p) #  gives (g**sk)%p
    return [pk,sk]

p=9993451781

g=3


pairKeys=KeyGen(p,g)

pk = pairKeys[0]

print("prime = ", p, "generator = ", g)
print("public key = ",pk)
