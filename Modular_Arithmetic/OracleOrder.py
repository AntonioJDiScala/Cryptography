def OracleOrder(a,N):
    import math
    d = math.gcd(a,N)
    if d!=1:
        print(a, "is non invertible mod", N)
        return d
    x = a
    j=1
    while x!=1:
        x = (x*a)%N
        j=j+1
    return j
