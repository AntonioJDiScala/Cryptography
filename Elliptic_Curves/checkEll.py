''' checkEll(P,a,b,q) = boolean True or False .
         according P=(x,y) belongs to
        the elliptic curve y^2 = x^3 + ax + b  (mod q)
'''
def checkEll(P,a,b,q):
    if P=="O":return True
    else:
        (x,y)=P
        z = (y**2 - (x**3 + a*x + b))%q
        if z==0: return True
        else: return False 
