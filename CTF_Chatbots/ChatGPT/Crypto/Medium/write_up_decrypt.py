from Crypto.Util.number import inverse, long_to_bytes

# Known values
n = 172433729131683
e = 65537
p = 132730129
q = 1299827

# Step 1: Compute phi
phi = (p - 1) * (q - 1)

# Step 2: Compute private key
d = inverse(e, phi)

# Step 3: Read ciphertext
c = int.from_bytes(open("cipher.bin", "rb").read(), 'big')

# Step 4: Decrypt
m = pow(c, d, n)
plaintext = long_to_bytes(m)
print(plaintext)
