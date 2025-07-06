from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import binascii

# Generate RSA key
key = RSA.generate(1024, e=3)
pubkey = key.publickey()

# Save public key
with open("public.pem", "wb") as f:
    f.write(pubkey.export_key())

# Encrypt the flag
flag = b"flag{low_exponent_rsa_attack}"
m = bytes_to_long(flag)
c = pow(m, pubkey.e, pubkey.n)

# Save ciphertext
with open("ciphertext.txt", "w") as f:
    f.write(hex(c)[2:])
