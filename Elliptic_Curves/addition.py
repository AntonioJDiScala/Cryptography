''' addition(P,Q,a,b,q) = (x3,y3) or "O".
         where (x3,y3) is the addition of (x1,y1) and (x2,y2) on
        the elliptic curve y^2 = x^3 + ax + b  (mod q).
'''
def addition(P,Q,a,b,q):
    from addpairs import addpairs
    #from inv import inv
    from checkEll import checkEll
    if P=="O": return Q
    elif Q=="O": return P
    else: return addpairs(P,Q,a,b,q)
   
