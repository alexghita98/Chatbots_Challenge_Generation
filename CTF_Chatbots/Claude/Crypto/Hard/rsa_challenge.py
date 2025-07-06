# Weak RSA implementation for educational purposes
p = 11
q = 13
n = p * q  # n = 143
e = 7

# Public key: (n, e) = (143, 7)
# Private key: d = 103 (calculated)

encrypted_flag = 26  # This decrypts to the flag when properly solved

print(f"Public key: n={n}, e={e}")
print(f"Encrypted flag: {encrypted_flag}")
print("Factor n to find p and q, then calculate the private key!")