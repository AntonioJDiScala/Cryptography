
m=7

a=4

mult = []
rema = []

for r in range(1,m):
    rema.append(r%m)
    mult.append((a*r)%m)

print(rema)
print(mult)
