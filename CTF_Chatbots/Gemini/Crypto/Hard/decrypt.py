def solve_xor_challenge(filepath):
    with open(filepath, 'rb') as f:
        encrypted_data = f.read()

    best_key = None
    max_spaces = -1
    decrypted_text = ""

    print("Attempting to find single-byte XOR key...")

    for key_candidate in range(256): # Iterate through all possible 256 byte values
        current_decrypted_bytes = bytearray()
        for byte_val in encrypted_data:
            current_decrypted_bytes.append(byte_val ^ key_candidate)

        # Count occurrences of space (ASCII 0x20)
        spaces_count = current_decrypted_bytes.count(0x20)

        # If this key produces more spaces than previous candidates, it's a better guess
        if spaces_count > max_spaces:
            max_spaces = spaces_count
            best_key = key_candidate
            # Try to decode as ASCII, ignore errors for unprintable characters during testing
            try:
                decrypted_text = current_decrypted_bytes.decode('ascii')
            except UnicodeDecodeError:
                decrypted_text = current_decrypted_bytes.decode('latin-1', errors='ignore') # Fallback

    if best_key is not None:
        print(f"\nLikely XOR Key: {hex(best_key)}")
        print(f"Decrypted Content (most probable):")
        print("-" * 50)
        print(decrypted_text)
        print("-" * 50)
        # Look for the flag in the decrypted text
        if "flag{" in decrypted_text and "}" in decrypted_text:
            start = decrypted_text.find("flag{")
            end = decrypted_text.find("}", start) + 1
            print(f"\nFound Flag: {decrypted_text[start:end]}")
        else:
            print("\nFlag not found in expected format. Examine the decrypted content closely.")
    else:
        print("Could not find a likely XOR key.")

# How to run:
solve_xor_challenge("encrypted.bin")