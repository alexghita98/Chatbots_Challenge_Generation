from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime, bytes_to_long

# Generate weak RSA key (512-bit)
p = getPrime(256)  # 256-bit prime
q = getPrime(256)  # 256-bit prime
n = p * q
e = 65537
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

key = RSA.construct((n, e, d))

# Save public key
with open("public_key.pem", "wb") as f:
    f.write(key.public_key().export_key())

# Encrypt flag
FLAG = b"FLAG{rsa_factorization_success}"
ciphertext = pow(bytes_to_long(FLAG), e, n)

with open("flag.enc", "wb") as f:
    f.write(ciphertext.to_bytes((ciphertext.bit_length()+7)//8, 'big'))