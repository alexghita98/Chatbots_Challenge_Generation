from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
import gmpy2

# Load ciphertext
with open("ciphertext.txt") as f:
    c = int(f.read(), 16)

# Load public key
with open("public.pem", "rb") as f:
    pubkey = RSA.import_key(f.read())

# Cube root attack
m, exact = gmpy2.iroot(c, pubkey.e)
if exact:
    print(long_to_bytes(m))
