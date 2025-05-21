''' addpairs(P,Q,a,b,q) = (x3,y3) or "O"
         where (x3,y3) is the addition of (x1,y1) and (x2,y2) on
        the elliptic curve y^2 = x^3 + ax + b  (mod q).
'''


def addpairs(P,Q,a,b,q):
    (x1,y1)=P
    (x2,y2)=Q
    #from inv import inv
    from checkEll import checkEll
    if checkEll(P,a,b,q)==True and checkEll(Q,a,b,q)==True:
        if x1%q==x2%q and y1%q==-y2%q:
          return "O"
        else:
            if x1%q != x2%q:
                lagreek = ((y2-y1)*pow(x2-x1,-1,q))%q
                nugreek = (y1 - lagreek*x1)%q
                x3 = (lagreek**2 - x1 - x2)%q
                y3 = (-(lagreek*x3+nugreek))%q
                R = (x3,y3)
                if checkEll(R,a,b,q)==True: return R
                else: return "error computing addition x1!=x2"
            else:
                lagreek = ((x1**2 + x1*x2 + x2**2 + a)*pow(y1+y2,-1,q))%q
                nugreek = (y1 - lagreek*x1)%q
                x3 = (lagreek**2 - x1 - x2)%q
                y3 = (-(lagreek*x3+nugreek))%q
                R = (x3,y3)
                if checkEll(R,a,b,q)==True: return R
                else: return "error computing addition x1==x2"
    else: return "error addition input"
   
