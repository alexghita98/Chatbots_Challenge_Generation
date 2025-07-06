import piexif
from PIL import Image

# Load a base JPEG image
img = Image.open("base.jpg")

# Create EXIF data with the flag in the UserComment field
exif_dict = {"Exif": {piexif.ExifIFD.UserComment: b"flag{exif_metadata_win}"}}
exif_bytes = piexif.dump(exif_dict)

# Save the image with the new EXIF data
img.save("photo.jpg", exif=exif_bytes)
