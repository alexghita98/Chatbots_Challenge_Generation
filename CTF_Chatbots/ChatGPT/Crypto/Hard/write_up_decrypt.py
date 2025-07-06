from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Known key used in the challenge setup
key = b"YELLOW SUBMARINE"  # 16 bytes for AES-128

# Read the ciphertext from file
with open("encrypted.bin", "rb") as f:
    ciphertext = f.read()

# Initialize AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt and unpad
plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted Message:")
print(plaintext.decode())
