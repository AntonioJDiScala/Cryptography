import secrets
hex_string = secrets.token_hex(32).upper()  # 256 bits = 32 bytes = 64 caracteres hexadecimales, pasados a mayusculas
print(hex_string)
