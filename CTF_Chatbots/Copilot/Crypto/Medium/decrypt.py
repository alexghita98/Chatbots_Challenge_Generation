import binascii

hex_data = "0d000c0c5e0e1a0c1c5e0e1a0c0c"
cipher_bytes = binascii.unhexlify(hex_data)

known = b"flag{"
key = bytes([cipher_bytes[i] ^ known[i] for i in range(3)])
print(f"Recovered key: {key}")

def xor_decrypt(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

plaintext = xor_decrypt(cipher_bytes, key)
print(plaintext.decode())