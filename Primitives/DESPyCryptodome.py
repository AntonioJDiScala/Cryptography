from Crypto.Cipher import DES

# key = b'-8B key-'

key = bytes(8)

cipher = DES.new(key, DES.MODE_ECB)

plaintext = bytes(8)

msg = cipher.encrypt(plaintext)

print(msg.hex())


plaindec = cipher.decrypt(msg)

print(plaindec.hex())

##plaintext = b'sona si latine loqueris '
##key = b'        '
##key = b'12345678'
