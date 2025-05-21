reg0 = [1,0,1]
reg=reg0
i = 0
print(i, "|",reg)
reg = [(reg[1]+reg[2])%2 , reg[0],reg[1]]
while reg !=reg0:
    i+=1
    print(i, "|",reg)
    reg = [(reg[1]+reg[2])%2 , reg[0],reg[1]]
    
