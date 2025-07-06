from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

key = b"YELLOW SUBMARINE"
msg = b"This is a secret message with flag{ecb_mode_does_not_hide_patterns} repeated repeated repeated"
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(msg, 16))

with open("encrypted.bin", "wb") as f:
    f.write(ciphertext)
