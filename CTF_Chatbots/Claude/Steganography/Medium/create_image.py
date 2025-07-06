from PIL import Image
import numpy as np

def create_lsb_image(message, output_path="hidden_message.png", image_size=(100, 100)):
    """
    Create an image with a hidden message using LSB steganography
    """
    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Add delimiter to mark end of message
    binary_message += '1111111111111110'  # Delimiter pattern
    
    # Calculate required image size
    min_pixels = len(binary_message)
    width, height = image_size
    
    # Ensure image is large enough
    if width * height < min_pixels:
        # Calculate new dimensions if needed
        width = int(np.ceil(np.sqrt(min_pixels)))
        height = width
        print(f"Adjusting image size to {width}x{height} to fit message")
    
    # Create a random-looking base image
    np.random.seed(42)  # For reproducible results
    img_array = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Hide message in LSBs of red channel
    message_index = 0
    for y in range(height):
        for x in range(width):
            if message_index < len(binary_message):
                # Get current pixel
                pixel = img_array[y, x]
                
                # Modify LSB of red channel
                red_value = pixel[0]
                # Clear LSB and set new bit
                red_value = (red_value & 0xFE) | int(binary_message[message_index])
                img_array[y, x, 0] = red_value
                
                message_index += 1
    
    # Convert numpy array to PIL Image and save
    img = Image.fromarray(img_array)
    img.save(output_path)
    print(f"Image saved as {output_path}")
    print(f"Hidden message: {message}")
    print(f"Message length: {len(message)} characters")
    print(f"Binary length: {len(binary_message)} bits")

def create_challenge_image():
    """Create the specific challenge image with the flag"""
    message = "FLAG{lsb_steganography_rocks}"
    create_lsb_image(message, "hidden_message.png", (50, 50))

# Alternative: Hide message in a real image
def hide_in_existing_image(message, input_image_path, output_path="hidden_message.png"):
    """
    Hide message in an existing image file
    """
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure RGB format
    pixels = img.load()
    width, height = img.size
    
    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Delimiter
    
    # Check if image is large enough
    if width * height < len(binary_message):
        raise ValueError(f"Image too small! Need at least {len(binary_message)} pixels")
    
    # Hide message in LSBs
    message_index = 0
    for y in range(height):
        for x in range(width):
            if message_index < len(binary_message):
                pixel = list(pixels[x, y])
                # Modify LSB of red channel
                pixel[0] = (pixel[0] & 0xFE) | int(binary_message[message_index])
                pixels[x, y] = tuple(pixel)
                message_index += 1
    
    img.save(output_path)
    print(f"Message hidden in {output_path}")

# Usage examples:
if __name__ == "__main__":
    # Create the challenge image
    create_challenge_image()
    
    # Or hide a custom message
    # create_lsb_image("Your secret message here!", "custom_hidden.png")
    
    # Or use an existing image (uncomment if you have a base image)
    # hide_in_existing_image("FLAG{lsb_steganography_rocks}", "base_image.png", "hidden_message.png")