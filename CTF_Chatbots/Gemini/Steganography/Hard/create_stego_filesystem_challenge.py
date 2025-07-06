import zipfile
import os

def create_polyglot_image_zip(image_path, flag_message, output_path):
    """
    Creates a ZIP archive containing the flag, and then appends it
    to an existing image file to create a polyglot file.
    """
    # 1. Ensure a base image exists
    #    You can use any JPG image. If you don't have one, PIL can create a dummy one.
    try:
        with Image.open(image_path) as img:
            img.save(image_path, "JPEG") # Ensure it's saved as JPEG if it was another format
    except Exception as e:
        print(f"'{image_path}' not found. Creating a placeholder image for demonstration.")
        from PIL import Image
        temp_img = Image.new('RGB', (600, 400), color = (50, 100, 150)) # Blueish color
        temp_img.save(image_path, "JPEG")
        print(f"Created '{image_path}'.")

    # 2. Create a temporary ZIP file containing the flag
    temp_zip_name = "temp_flag.zip"
    flag_filename_in_zip = "flag.txt"
    with zipfile.ZipFile(temp_zip_name, 'w') as zf:
        zf.writestr(flag_filename_in_zip, flag_message)
    print(f"Created temporary ZIP file: {temp_zip_name}")

    # 3. Concatenate the image and the ZIP file
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    with open(temp_zip_name, 'rb') as zip_file:
        zip_data = zip_file.read()

    with open(output_path, 'wb') as output_file:
        output_file.write(image_data)
        output_file.write(zip_data)
    
    print(f"Polyglot image-zip created: {output_path}")

    # Clean up temporary ZIP file
    os.remove(temp_zip_name)
    print(f"Removed temporary ZIP file: {temp_zip_name}")

if __name__ == "__main__":
    # 1. Provide a base JPG image. You can use any JPG.
    #    Let's assume you've placed 'base_image.jpg' in the same directory.
    #    If not, the script will create a simple one.
    
    base_image_file = "base_image.jpg" # Path to your base image (JPG recommended)
    flag_to_hide = "flag{hidden_data_at_the_end}"
    output_challenge_file = "challenge_polyglot.jpg"

    create_polyglot_image_zip(base_image_file, flag_to_hide, output_challenge_file)
    print(f"Challenge created: {output_challenge_file}")