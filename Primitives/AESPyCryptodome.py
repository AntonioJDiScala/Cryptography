# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

# C:\Program Files\Python311>python.exe -m idlelib.idle

# Example and benchmark from : https://www.kavaliro.com/wp-content/uploads/2014/03/AES.pdf


# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


# Funzione per cifrare un testo
def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Inizializza il cifrario AES in modalità ECB
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # Cifra il testo
    return ciphertext  # Restituisce il ciphertext codificato in base64

# Funzione per decifrare un testo
def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Crea il cifrario AES 
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size) # Decifra il testo
    return plaintext.decode()

# Esempio d'uso

key1 = "Thats my Kung Fu"
key = key1.encode('utf-8')

print(key)

#key = get_random_bytes(16)  # Genera una chiave random di 16 byte (AES-128)

### the plaintext to be encrypted
##file = open('Satoshi.txt', 'r')
##plaintext = file.read()

plaintext="Two One Nine Two"

# Plaintext
print("Plaintext:")
print(plaintext)



# Cifratura
ciphertext = encrypt(plaintext, key)
print("Ciphertext:")
print(ciphertext.hex())

print("-------------------------")
print("-------------------------")

# Decifratura
decrypted_text = decrypt(ciphertext, key)
print("Plaintext:")
print(decrypted_text)


print("-------------------------")
print("-------------------------")

# Key  e.g. d1 54 3e 26 3c fa 89 b9 c8 1d 66 9e 86 ed af 62
print(key.hex())


