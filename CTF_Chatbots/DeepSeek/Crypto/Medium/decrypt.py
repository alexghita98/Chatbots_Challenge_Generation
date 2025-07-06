with open('encrypted.bin', 'rb') as f:
    ciphertext = f.read()

for key in range(256):  # Try all possible 1-byte keys
    plaintext = bytes([b ^ key for b in ciphertext])
    if b'FLAG{' in plaintext:  # Look for flag pattern
        print(f"Key: {hex(key)}")
        print(f"Message: {plaintext.decode()}")
        break