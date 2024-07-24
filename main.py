import os.path

from PIL import Image
import matplotlib.pyplot as plt

# Open the original image
img = Image.open('AAA.jpg')

# Display the original image
plt.imshow(img)
plt.title('Original Image')
plt.show()

# Compress the image (quality=50 is a good balance between quality and size)
img_compressed = img.convert('RGB')
width, height = img.size
new_size = (width//2, height//2)
resized_image = img.resize(new_size)
img_compressed.save('compressed_image.jpg', quality=100, optimize=True)

# Open the compressed image
img_compressed = Image.open('compressed_image.jpg')

# Display the compressed image
plt.imshow(img_compressed)
plt.title('Compressed Image')
plt.show()

print(os.path.getsize('AAA.jpg'))
print(os.path.getsize('compressed_image.jpg'))
