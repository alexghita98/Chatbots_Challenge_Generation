from PIL import Image
import numpy as np

def encode_lsb(image_path, secret_message, output_path):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    # Convert message to binary
    binary_msg = ''.join([format(ord(c), '08b') for c in secret_message])
    binary_msg += '00000000'  # Null terminator
    
    # Embed in LSBs
    msg_index = 0
    for row in pixels:
        for pixel in row:
            for color in range(3):  # R,G,B channels
                if msg_index < len(binary_msg):
                    pixel[color] = (pixel[color] & 0xFE) | int(binary_msg[msg_index])
                    msg_index += 1
    
    Image.fromarray(pixels).save(output_path)

# Usage
original_image = "original.png"  # Any clean image
secret_message = "FLAG{lsb_stealthy}"
encode_lsb(original_image, secret_message, "lsb_encoded.png")