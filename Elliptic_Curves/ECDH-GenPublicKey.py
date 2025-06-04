#
# Here a Python implementation of the Public_Key Generator for the Diffie-Hellman protocol
#  using the Bitcoin elliptic curve Secp256k1.
#
#  Bitcoin https://en.bitcoin.it/wiki/Secp256k1
#
#  Input: the hexadecimal of the Secret_Key  (see bellow)
#
#  Output:  the Public_Key i.e. a point on the elliptic curve such that:
#
#                      Secret_Key . G = Public_Key
#
#           The output is written in the file "myPublic_Key.txt" 
#



from multB import multB


#
# Secpt256k1   domani parameter see e.g. https://www.secg.org/sec2-v2.pdf

Gx='79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798'
Gy='483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8'
p='FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F'
a=0
b=7

G=(int(Gx,16),int(Gy,16))
q=int(p,16)

#
#
# The Secret_Key is string type with the hexadecimal representation of a number of 256 bit. Namely, 32 bytes.
#
#  you should construct your Secret_Key using a RND offline e.g. by tossing a coin or dices,
#  convert it to hexadecimal and paste it here below.
#
#  Warning: your Secret_Key must have 64 hexadecimal digits no more nor less!
#

Secret_Key = '83ED02B1B7214E2786C2F111310434EF8237EC07A70E48F6291AF911B821784'  # e.g. '1B046BDCDFC42A2F65758DC9CFFA0E60F20F9D4662700C6AFF8BBDD28B9EF39D'

#
#  Below we compute the public 
#
#

SKdec = int(Secret_Key, 16)
SKbin = bin(SKdec)[2:]

Public_Key = multB(SKbin,G,a,b,q)

XPK = format(Public_Key[0],'064X')
YPK = format(Public_Key[1],'064X')
print(XPK,len(XPK))
print(YPK, len(YPK))

wPK = '04'+XPK+YPK


File = open('myPublic_Key.txt','w')
File.write(wPK)
File.close()

print("finito, your public file is in the file myPublic_Key.txt ")


