from PIL import Image
import requests
from io import BytesIO

url_image = 'https://4kwallpapers.com/images/wallpapers/cyberpunk-mclaren-supercars-neon-art-3840x2160-1003.jpg'

response = requests.get(url_image)

img = Image.open(BytesIO(response.content))

width = img.size[0]
height = img.size[1]

matrix_pixels = img.load()

for i in range(width): 
    for j in range(height): 
        pixel = matrix_pixels[i,j]
        R = pixel[0]
        G = pixel[1]
        B = pixel[2]
        
        R = G = B = int((R*0.299 + G*0.587 + B*0.114))
       
        new_pixel = (R,G,B)
        matrix_pixels[i,j] = new_pixel


img.show()