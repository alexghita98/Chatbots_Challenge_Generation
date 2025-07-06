from PIL import Image
import numpy as np

def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    binary_msg = ""
    for row in pixels:
        for pixel in row:
            for color in range(3):  # R,G,B
                binary_msg += str(pixel[color] & 1)
    
    # Split into 8-bit chunks
    chars = []
    for i in range(0, len(binary_msg), 8):
        byte = binary_msg[i:i+8]
        if byte == '00000000':
            break
        chars.append(chr(int(byte, 2)))
    
    return ''.join(chars)

print(decode_lsb("lsb_encoded.png"))