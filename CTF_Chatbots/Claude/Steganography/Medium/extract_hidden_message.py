from PIL import Image

def extract_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size
    
    binary_data = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            # Extract LSB from red channel
            binary_data += str(pixel[0] & 1)
    
    # Convert binary to text
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            if char.isprintable():
                message += char
    
    return message

# Usage
result = extract_lsb("hidden_message.png")
print(result)