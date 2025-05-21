from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

def salsa20_encrypt(plaintext, key, nonce):
    # Create a Salsa20 cipher object with the given key
    cipher = Salsa20.new(key, nonce=nonce)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)
    
    return ciphertext

def salsa20_decrypt(ciphertext, key, nonce):
    # Create a Salsa20 cipher object with the given key and nonce
    cipher = Salsa20.new(key, nonce=nonce)
    
    # Decrypt the ciphertext
    decrypted = cipher.decrypt(ciphertext)
    
    return decrypted

def format_hex(ciphertext):
    # Format the ciphertext in hexadecimal, grouping bytes by 4
    return ' '.join(ciphertext[i:i+4].hex() for i in range(0, len(ciphertext), 4))


# Main code
if __name__ == "__main__":
    # Define the plaintext and the key
    plaintext = bytes(64)
    key = bytes(32)  # Salsa20 requires a 32-byte key

    # Encrypt the plaintext
    nonce = bytes(8)
    ciphertext = salsa20_encrypt(plaintext, key, nonce)
    print("Ciphertext (hex):", format_hex(ciphertext))

    # Decrypt the ciphertext
    decrypted = salsa20_decrypt(ciphertext, key, nonce)
    print("Decrypted text:", decrypted)
