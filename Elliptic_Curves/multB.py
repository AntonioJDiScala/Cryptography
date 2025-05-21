''' multB(n,P,a,b,q) = (x1,y1) .
        where (x1,y1) is the addition of P n-times on  
        the elliptic curve y^2 = x^3 + ax + b  (mod q)
        n is passed as a string of bits
'''

def multB(n,P,a,b,q):
    from checkEll import checkEll
    from addition import addition
    if P=="O": return "O"    
    if checkEll(P,a,b,q)==False: return "(x,y) not in Ell"
    else:
        T="O"
        bina=n
        for d in bina:
            T=addition(T,T,a,b,q)
            if d=='1': T=addition(T,P,a,b,q)
        return T
        
 
