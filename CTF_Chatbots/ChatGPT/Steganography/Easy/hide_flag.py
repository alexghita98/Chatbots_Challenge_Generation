from stegano import lsb
from PIL import Image

# Create a blank image (or use an existing BMP)
img = Image.new("RGB", (300, 300), color="white")
img.save("cover.bmp")

# Hide the flag in the image using LSB
secret = lsb.hide("cover.bmp", "flag{basic_lsb_extraction}")
secret.save("hidden_message.bmp")
