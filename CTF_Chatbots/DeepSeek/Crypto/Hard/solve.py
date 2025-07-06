from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
import gmpy2

# Load public key
with open("public_key.pem", "rb") as f:
    key = RSA.import_key(f.read())
    n = key.n
    e = key.e

# Factorize n (using Fermat's method)
def factor(n):
    a = gmpy2.isqrt(n) + 1
    b = a*a - n
    while not gmpy2.is_square(b):
        a += 1
        b = a*a - n
    p = a - gmpy2.isqrt(b)
    q = n // p
    return int(p), int(q)

p, q = factor(n)
print(f"Found primes:\np = {p}\nq = {q}")

# Calculate private exponent
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

# Decrypt flag
with open("flag.enc", "rb") as f:
    c = int.from_bytes(f.read(), 'big')

m = pow(c, d, n)
print("Decrypted flag:", long_to_bytes(m).decode())