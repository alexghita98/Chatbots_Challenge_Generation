def calculate_checksum_py(input_str):
    checksum = 0xABCDEF01 # Initial seed
    for char_val in input_str.encode('utf-8'): # Ensure bytes
        checksum = (checksum + char_val) * 0x1000193
        checksum &= 0xFFFFFFFF # Ensure 32-bit unsigned
        checksum ^= (checksum >> 16)
        checksum &= 0xFFFFFFFF # Ensure 32-bit unsigned
    return checksum

secret_data = "super_secret_payload_for_checksum"
expected_checksum_val = calculate_checksum_py(secret_data)
print(f"Expected Checksum (decimal): {expected_checksum_val}")
print(f"Expected Checksum (hex): {hex(expected_checksum_val)}")
# This will output something like: Expected Checksum (hex): 0x6191b92d