from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from piexif import dump, insert, ExifIFD, GPSIFD, ImageIFD

def create_image_with_custom_exif(output_path, flag_message):
    """
    Creates a simple image and embeds custom EXIF data, including the flag.
    Requires piexif library: pip install piexif
    """
    # Create a simple blank image
    img = Image.new('RGB', (400, 300), color = (150, 150, 150)) # Grey image

    # Define EXIF data structure
    # Use standard EXIF tags, some of which are often populated by cameras
    # 0th IFD contains basic image information
    zeroth_ifd = {
        ImageIFD.Make: b"CTF-Maker",
        ImageIFD.Model: b"SteganoChallenge-V1",
        ImageIFD.Software: b"Pillow-Piexif",
        ImageIFD.Artist: b"The CTF Team",
        ImageIFD.Copyright: b"2025 CTF",
        ImageIFD.DateTime: b"2025:07:04 12:00:00",
    }

    # Exif IFD contains more specific image data and sometimes user comments
    exif_ifd = {
        ExifIFD.DateTimeOriginal: b"2025:07:04 11:59:00",
        ExifIFD.ExifVersion: b"0220",
        # Store the flag in UserComment which belongs in the Exif IFD
        ExifIFD.UserComment: flag_message.encode('utf-8') 
    }

    # Combine into the full EXIF dictionary
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd}
    exif_bytes = dump(exif_dict)

    # Save the image with the EXIF data
    img.save(output_path, exif=exif_bytes)
    print(f"Image with hidden metadata created: {output_path}")

if __name__ == "__main__":
    # Ensure piexif is installed: pip install piexif
    flag_to_hide = "flag{exif_exposure}"
    output_image_file = "challenge_metadata.jpg"
    
    create_image_with_custom_exif(output_image_file, flag_to_hide)
    print(f"Challenge created: {output_image_file}")