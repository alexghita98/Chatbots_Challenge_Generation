from PIL import Image

def hide_message_in_lsb(image_path, message, output_path):
    """
    Hides a string message in the LSB of the blue channel of an image.
    Works by adjusting the last bit of each blue pixel component.
    Assumes RGB or RGBA image.
    """
    img = Image.open(image_path).convert("RGB") # Ensure RGB mode
    width, height = img.size
    
    # Convert message to binary string
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Add a null terminator (8 zeros) to indicate end of message
    binary_message += '00000000' 

    if len(binary_message) > width * height:
        print("Error: Message too long for image size!")
        return

    data_index = 0
    new_img = Image.new(img.mode, img.size)
    pixels = new_img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            if data_index < len(binary_message):
                # Change the LSB of the blue component
                # Current LSB of blue: b % 2
                # Target LSB: int(binary_message[data_index])
                # Adjust blue component: (b & ~1) sets LSB to 0, then add target LSB
                b = (b & ~1) | int(binary_message[data_index])
                data_index += 1
            
            pixels[x, y] = (r, g, b)

    new_img.save(output_path, "PNG")
    print(f"Message hidden successfully in {output_path}")

if __name__ == "__main__":
    # 1. Provide a base image. This should be a common image format, PNG is ideal.
    #    You can use any PNG image you have, or download a sample one (e.g., a landscape photo).
    #    Make sure 'carrier_image.png' exists in the same directory as this script.
    #    Example: A simple solid color image if you don't have one handy:
    #    from PIL import Image
    #    img = Image.new('RGB', (200, 200), color = 'red')
    #    img.save('carrier_image.png')
    
    #    For a more realistic challenge, use a photo.
    #    Let's assume you've placed 'carrier_image.png' in the same directory.
    
    carrier_image_file = "carrier_image.png" # Path to your base image
    flag_to_hide = "flag{lsb_is_simple}"
    output_challenge_image = "challenge_image.png"

    # Important: Create a simple carrier_image.png if you don't have one
    # If you have a real image, comment out these lines:
    try:
        Image.open(carrier_image_file)
    except FileNotFoundError:
        print(f"'{carrier_image_file}' not found. Creating a placeholder image for demonstration.")
        temp_img = Image.new('RGB', (100, 100), color = (100, 150, 200)) # A blueish color
        temp_img.save(carrier_image_file)
        print(f"Created '{carrier_image_file}'.")


    hide_message_in_lsb(carrier_image_file, flag_to_hide, output_challenge_image)
    print(f"Challenge created: {output_challenge_image}")