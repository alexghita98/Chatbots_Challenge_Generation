from PIL import Image
import stepic

# Create a clean image
img = Image.new('RGB', (300, 200), color='white')

# Hide the flag
secret_message = "FLAG{stegan0_101}"
img_with_secret = stepic.encode(img, secret_message.encode())

# Save the image
img_with_secret.save('secret_image.png')
print("Challenge image generated!")