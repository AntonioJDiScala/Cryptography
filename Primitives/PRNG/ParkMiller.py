# Park - Miller RNG 
#
# https://www.youtube.com/watch?v=EXsLyfqwopg
#
# http://www.firstpr.com.au/dsp/rand31/p1192-park.pdf

s = 1
a = 7**5
tp=2**31
m=tp-1
i=1
while i < 10002:
    print(i,s)
    s = (a*s)%m
    i+=1
