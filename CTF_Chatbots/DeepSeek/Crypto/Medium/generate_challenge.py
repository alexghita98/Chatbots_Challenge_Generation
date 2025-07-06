# Generate the encrypted file
flag = "FLAG{xor_cool}"
plaintext = f"The flag is {flag}".encode()
key = 0x37

ciphertext = bytes([b ^ key for b in plaintext])
with open("encrypted.bin", "wb") as f:
    f.write(ciphertext)