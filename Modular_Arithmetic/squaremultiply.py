def squaremultiply(a,n,q):
    bina='{0:b}'.format(n)
    T=1
    amq=a%q
    for d in bina:
        T=(T*T)%q
        if d=='1': T=(T*amq)%q
    return(T)
    
