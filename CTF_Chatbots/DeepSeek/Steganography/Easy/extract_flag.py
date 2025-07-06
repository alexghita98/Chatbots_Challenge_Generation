from PIL import Image
import stepic

img = Image.open('secret_image.png')
print(stepic.decode(img))