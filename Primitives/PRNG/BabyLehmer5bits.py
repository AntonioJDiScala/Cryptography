# Baby LCG Lehmer 5 bits.
# f(u)=a*u + b  (mod 2^5)

s=1
a=7
b=5
i=s
while i < 33:
    print(i,'{0:05b}'.format(s))
    s=((a*s)+b)%32
    i+=1
