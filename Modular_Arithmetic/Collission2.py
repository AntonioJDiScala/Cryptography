from timeit import default_timer as timer

from random import randrange

import math


from SqM import squaremultiply



#---------------Data-----------------------------------------------------

pk=3424750084

p=9993451781

lbp = math.ceil(math.log(p,2))

g=3

gOrd = p-1

print("prime = p = ", p, "bits of p=", lbp )
print("public key = ", pk)
print("generator = g = ", g)

#import primefac
#list(primefac.primefac(p-1))

#-----------------------------------------------------------------------




t = lbp//2

ccc = math.ceil(math.sqrt(math.log(4)))



pt=(2**t)*ccc
start = timer()
j=0
lista = []
pairs = []
flag = True

print("stima = ", math.sqrt(p)*ccc)
print("iterations = ", pt)

while j < pt and flag:
    a = randrange(gOrd)
    b = randrange(gOrd)
    m = (squaremultiply(g,a,p)*squaremultiply(pk,b,p))%p
    if m in lista:
        dove = lista.index(m)
        A = pairs[dove][0]
        B = pairs[dove][1]
        Bmb = (B-b)%gOrd
        amA = (a-A)%gOrd
        dis=math.gcd(Bmb,gOrd)
        if amA%dis == 0:
                   print("Done!")          
                   Bmb1 = Bmb//dis
                   amA1 = amA//dis
                   gOrd1 = gOrd//dis
                   invBmb1 = pow(Bmb1,-1,gOrd1)
                   xo = (invBmb1*amA1)%(gOrd1)
                               #  xo is a solution of: Bmb1.x = amA1 (mod gOrd1)
                               #and so also of Bmb.x = amA (mod gOrd)
                               # so xo and the sk satisfies :
                               #   Bmb(sk-xo)=0 (mod gOrd) .
                               # Then:
                               #   sk = xo + k * gOrd1  , k=0,1,...,(dis-1) 
                               #
                         #Here we look for k such that pk = g**(xo+k*gOrd1)  (mod gOrd)      
                   flag1 = True
                   k=0
                   while k < dis and flag1:
                             xs = xo + k*gOrd1
                             if squaremultiply(g,xs,p)==pk:
                                 flag1=False
                                 print("secret key = " ,xs)
                                 print("public key = ", pk)
                             else:
                                 k=k+1
                   flag = False
    else:
        lista.append(m)
        pairs.append((a,b))
    j+=1
    if j%10000==0: print(j,len(lista),len(pairs))
    
end = timer()
mm = (end - start)/60
#print the total time employed to check all keys
print(t, mm ,"minutes") # Time in minutes.
print("number of pairs = ", len(lista),"==",len(pairs))

