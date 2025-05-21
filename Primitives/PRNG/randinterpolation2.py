s = 1
a = 7**5
tp=2**31
m=tp-1
i=1
while i < 10:
    print(s)
    s = (a*s)%m
    i+=1
