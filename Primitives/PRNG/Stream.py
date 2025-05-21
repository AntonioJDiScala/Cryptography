reg = [1,0,1]
clock = "1"
while clock != "Exit":
    clock = input("")
    print(reg[2])
    reg = [(reg[1]+reg[2])%2 , reg[0],reg[1]]
    
