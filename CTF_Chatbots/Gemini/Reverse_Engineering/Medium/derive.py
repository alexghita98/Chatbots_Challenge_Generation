obfuscated_bytes = [0x23, 0x27, 0x34, 0x27, 0x30, 0x31, 0x27, 0x2f, 0x27, 0x00]
xor_key = 0x42

plaintext_password = ""
for byte_val in obfuscated_bytes:
    if byte_val == 0x00: # Stop at null terminator
        break
    plaintext_password += chr(byte_val ^ xor_key)

print(f"The correct password is: {plaintext_password}")
# Output will be: The correct password is: reverseme