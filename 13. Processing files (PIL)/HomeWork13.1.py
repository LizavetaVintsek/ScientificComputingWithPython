from PIL import Image

image1 = Image.open('image.png')
print (image1.mode)
# RGB
print (image1.size)
# (2304, 1344)
print (image1.format)
# PNG
with image1 as im:
    im.thumbnail((128, 128))
    im.save('image_thumbnail.jpg', "JPEG")
