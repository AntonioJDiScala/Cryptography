#
# Here a Python implementation of the common secret of Diffie-Hellman protocol
#  using the Bitcoin elliptic curve Secp256k1.
#
#  Bitcoin https://en.bitcoin.it/wiki/Secp256k1
#
#  Input:
#          1) the hexadecimal string of my_Secret_Key  (see bellow)
#          2) the Public_Key_Friend of the other party as string in noncompressed form e.g. "04A83C5C475498F46A402CB0B18CF195ABA2CD809787334B2770E57D07ABAAC0EB52A8AE496BA6989CE0ACBCE786BEAF556BFC1780E5795139B0D352691DAC1725"
#               keep in mind that the initial "04.." indicates the unoncompressed form.
#
#  Output:  the common secret i.e. a point on the elliptic curve such that:
#
#                      Secret_Key . Public_Key = Common_Secret
#
#           The output is written in the file "Common_Secret.txt" 
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
#  convert it to hexadecimal and paste it here below
#

my_Secret_Key = ''  # e.g. '1B046BDCDF542A2F65758DC9CFFA0E60F20F9D4662700C6A338BBDD28B9EF39D'

#
#
#  The Public_Key of the person you are exchanging public keys:
#
#

Public_Key_Friend = '04D9E15C880EAA4DA95C6581C975210EEED700CFC11275B291ADEF516D2567604C269402ECCDCE237A4CDB33339271882CA4F83EA7D2522633B0568BE35FC6A14C'

#
#  Below we compute the common secret with your friend
#
#

substringX = Public_Key_Friend[2:66]
substringY = Public_Key_Friend[66:131]

FriendPK =(int(substringX,16),int(substringY,16))

SKdec = int(my_Secret_Key, 16)
SKbin = bin(SKdec)[2:]

Common_Secret = multB(SKbin,FriendPK,a,b,q)

XPK = format(Common_Secret[0],'064X')
YPK = format(Common_Secret[1],'064X')

wPK = '04'+XPK+YPK


File = open('Common_Secret.txt','w')
File.write(wPK)
File.close()

print("finito, the common secret with your friend is in the file Common_Secret ")


