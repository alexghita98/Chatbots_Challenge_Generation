import sys

def xor_data(data, key_byte):
    """XORs bytes with a repeating single-byte key."""
    return bytes([b ^ key_byte for b in data])

if __name__ == "__main__":
    plaintext_message = b"This is a secret message. The flag is flag{xor_is_fun_but_weak}."
    
    # Choose a single-byte key (e.g., 0xDE). Avoid 0x00 as it wouldn't encrypt.
    # Also avoid keys that make too many characters unprintable, though frequency analysis should still work.
    xor_key = 0xDE 

    encrypted_data = xor_data(plaintext_message, xor_key)

    with open("encrypted.bin", "wb") as f:
        f.write(encrypted_data)

    print(f"Generated encrypted.bin with plaintext: '{plaintext_message.decode()}' and XOR key: {hex(xor_key)}")
    print(f"Size of encrypted.bin: {len(encrypted_data)} bytes")