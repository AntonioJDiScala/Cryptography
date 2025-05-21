
#10, 6, 2

m = 125

b=10

Powers = []




i=0
while True:
    pt = (b**i)%m
    if pt in Powers:
        print("last power =", pt)
        break
    Powers.append(pt)
    i=i+1
print("List of Powers =", Powers)
    


##Observations:
##
##1) Notice the difference of the length of the set of powers.
##   Such length is called "order" or period $b$ (mod m).
##
##2) Notice that the multiplication of two powers is again a power.
##   So the set of powers is "closed" under multiplication.
