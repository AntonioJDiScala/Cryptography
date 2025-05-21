reg0 = [1,0,0,0]
reg=reg0
i = 0
print(i, "|",reg)
reg = [(reg[0]+reg[3])%2 , reg[0],reg[1],reg[2]]
while reg !=reg0:
    input()
    i+=1
    print(i, "|",reg)
    reg = [(reg[0]+reg[3])%2 , reg[0],reg[1],reg[2]]
    
### Mirror


##reg0 = [1,0,0,1]
##reg=reg0
##i = 0
##print(i, "|",reg)
##reg = [(reg[2]+reg[3])%2 , reg[0],reg[1],reg[2]]
##while reg !=reg0:
##    input()
##    i+=1
##    print(i, "|",reg)
##    reg = [(reg[2]+reg[3])%2 , reg[0],reg[1],reg[2]]    
