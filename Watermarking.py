from PIL import Image
from scipy.fft import fftshift, ifftshift, ifft2, fft2
import numpy as np
import cv2
def watermark_with_transparency(base_image,
                                watermark_image_path,
                                position,
                                ratio = 5):
    # Base Image(Ảnh bị chèn )

    # Watermark image and convert image to alpha channel (Ảnh để đánh dấu)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    # Extract width and height of the base image(Lấy chiều cao, chiều rộng của ảnh)
    width, height = base_image.size
    #Resize watermark depends on the ratio of the size of the base image(Chỉnh kích cỡ của ảnh)
    watermark = watermark.resize((int(width/ratio),int(height/ratio)))
    # create a new image using the same width and height as the image we are watermarking
    # You will note that this image that we create is RGBA which means it has Red, Green and Blue with Alpha.
    # Tạo 1 ảnh nền có kích cỡ bằng kích cỡ của base image để chèn 2 ảnh
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    # paste in the image we want to watermark starting at the upper left, which is (0,0)
    transparent.paste(base_image, (0,0))
    # Paste in our watermark using the passed in position and we also mask the watermark with itself
    transparent.paste(watermark, position, mask=watermark)
    # Show Image
    #transparent.show()

    # Save transparent image to file png (PNG is the reasonable choice for the alpha channel)
    # If it's got an alpha channel that you want to preserve, PNG is really the only reasonable choice.
    # Alternately you can flatten it to a RGB image and save as a JPEG.
    # https://stackoverflow.com/questions/9166400/convert-rgba-png-to-rgb-with-pil
    #transparent.save(output_image_path, format="png")


    return transparent
def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path,
                    position):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    # add watermark to your image
    base_image.paste(watermark, position)
    base_image.show()
    base_image.save(output_image_path)
# This function used to move the watermark image to corner or center of the base image
def watermark_with_transparency_pos(base_image,
                                watermark_image_path,
                                position = 'center', ratio = 5):
    width_base, height_base = base_image.size
    # Set position based on the size of the base_image
    output = None
    if position == "upper left":
        output = watermark_with_transparency(base_image,  watermark_image_path,
                                    position=(0, 0) , ratio= ratio)
    elif position == "upper right":
        output = watermark_with_transparency(base_image,  watermark_image_path,
                                    position=(int(width_base-width_base/ratio), 0) , ratio= ratio)
    elif position == "lower left":
        output = watermark_with_transparency(base_image,  watermark_image_path,
                                    position=(0, int(height_base-height_base/ratio)) , ratio= ratio)
    elif position == "lower right":
        output = watermark_with_transparency(base_image,  watermark_image_path,
                                    position=(int(width_base-width_base/ratio), int(height_base-height_base/ratio)) , ratio= ratio)
    elif position == "center":
        output = watermark_with_transparency(base_image,  watermark_image_path,
                                    position=(int((width_base-width_base/ratio)/2), int((height_base-height_base/ratio)/2)) , ratio= ratio)
    return output

def overlayImage(base_image_after, watermark_image_after, position, ratio = 0.2):
    w_base, h_base = base_image_after.size

    # Resize watermark based on ratio of size of base image
    if ratio <= 0  or ratio > 1 :
        ratio = 0.2
    watermark_image_after = watermark_image_after.resize((int(w_base*ratio), int(h_base*ratio)))
    w_water, h_water = watermark_image_after.size

    x, y = position
    if x + w_water > w_base:
        x = w_base - w_water
    elif x < 0:
        x = 0
    if y + h_water > h_base:
        y = h_base - h_water
    elif y < 0:
        y = 0
    base_image_after = np.asarray(base_image_after, dtype="int32")
    watermark_image_after = np.asarray(watermark_image_after, dtype="int32")
    base_image_after[y : y + h_water, x : x + w_water] = watermark_image_after
    # X is width, Y is height
    pillowOutput = np.around(base_image_after).astype(np.uint8)
    pillowOutput = Image.fromarray(pillowOutput)
    pillowOutput.show()
    return pillowOutput
def visibleWatermark(base_image,
                    watermark_image_path, alpha = 0.5):
    base_image = base_image.convert('RGB')
    width, height = base_image.size

    watermark = Image.open(watermark_image_path).convert('RGB')
    watermark = watermark.resize((int(width), int(height)))


    base_image = np.asarray(base_image, dtype="int32")
    watermark = np.asarray(watermark, dtype="int32")

    watermarked_image = np.dot((1 - alpha), base_image) + np.dot(alpha,watermark)
    watermarked_image = np.around(watermarked_image).astype(np.uint8)
    watermarked_image = Image.fromarray(watermarked_image)
    watermarked_image.show()
    return watermarked_image
def visibleWatermark_with_Pos(base_image,
                    watermark_image_path, position, ratio = 0.2, alpha = 0.5):
    base_image = base_image.convert('RGB')
    width, height = base_image.size
    if ratio <= 0  or ratio > 1 :
        ratio = 0.2
    watermark = Image.open(watermark_image_path).convert('RGB')
    watermark = watermark.resize((int(width*ratio), int(height*ratio)))
    w_water, h_water = watermark.size

    x, y = position
    if x + w_water > width:
        x = width - w_water
    elif x < 0:
        x = 0
    if y + h_water > height:
        y = height - h_water
    elif y < 0:
        y = 0

    base_image = np.asarray(base_image, dtype="int32")
    watermark = np.asarray(watermark, dtype="int32")
    base_image_after = np.dot((1 - alpha), base_image)
    watermark_after = np.dot(alpha,watermark)

    base_image_after[y: y + h_water, x: x + w_water] += watermark_after
    watermarked_image = np.around(base_image_after).astype(np.uint8)
    watermarked_image = Image.fromarray(watermarked_image)
    return watermarked_image
def invisibleWatermark_with_Pos(base_image,watermark_image_path, position, ratio = 0.2):
    base_image = base_image.convert('RGB')
    width, height = base_image.size
    if ratio <= 0 or ratio > 1:
        ratio = 0.2
    watermark = Image.open(watermark_image_path).convert('RGB')
    watermark = watermark.resize((int(width * ratio), int(height * ratio)))
    w_water, h_water = watermark.size
    x, y = position
    if x + w_water > width:
        x = width - w_water
    elif x < 0:
        x = 0
    if y + h_water > height:
        y = height - h_water
    elif y < 0:
        y = 0
    base_image = np.asarray(base_image, dtype="int32")
    watermark = np.asarray(watermark, dtype="int32")
    base_image_after = 4*(np.dot(base_image, 1/4))
    watermark_after = np.dot(watermark,1/64)
    base_image_after[y: y + h_water, x: x + w_water] += watermark_after
    watermarked_image = np.around(base_image_after).astype(np.uint8)
    watermarked_image = Image.fromarray(watermarked_image)
    #watermarked_image.show()
    return watermarked_image
def invisibleWatermark(base_image,
                    watermark_image_path):
    base_image = base_image.convert('RGB')
    width, height = base_image.size

    watermark = Image.open(watermark_image_path).convert('RGB')
    watermark = watermark.resize((int(width), int(height)))

    base_image = np.asarray(base_image, dtype="int32")
    watermark = np.asarray(watermark, dtype="int32")
    watermarked_image = 4*(np.dot(base_image, 1/4)) + np.dot(watermark,1/64)
    watermarked_image = np.around(watermarked_image).astype(np.uint8)
    watermarked_image = Image.fromarray(watermarked_image)

    #watermarked_image.show()
    return watermarked_image
# Set intensity to full intensity range
def extract_invisilbeWatermark(base_image, watermarkedImage, intensity = 30):
    base_image = np.asarray(base_image, dtype="int32")
    watermarkedImage = np.asarray(watermarkedImage, dtype="int32")
    watermark = np.dot((2**6) * np.dot(watermarkedImage - base_image,1/(2**6)), intensity)
    watermark = np.around(watermark).astype(np.uint8)
    watermark = Image.fromarray(watermark)
    #watermark.show()
    return watermark
def extract_visibleWatermark(base_image, watermarkedImage, alpha = 0.5):
    base_image = np.asarray(base_image, dtype="int32")
    watermarkedImage = np.asarray(watermarkedImage, dtype="int32")
    watermark = np.dot(watermarkedImage - np.dot((1 - alpha), base_image), 1/alpha)
    watermark = np.around(watermark).astype(np.uint8)
    watermark = Image.fromarray(watermark)
    #watermark.show()
    return watermark
def main():
    # base image
    img = "Resources/background.jpg"
    watermark_path = 'Resources/7logo.png'
    # Watermark image to base image
    base_image = Image.open(img)
    #base_image.show()
    #watermark = Image.open(watermark_path)
    #watermark.show()

    #overlay_Image = overlayImage(base_image,water_image, (0,0), ratio=1/5)
    #visibleWatermarked = visibleWatermark(base_image, watermark_path, alpha=0.2)
    visible_with_Pos = visibleWatermark_with_Pos(base_image,
                    watermark_path, (0,0), ratio = 0.2, alpha = 0.5)
    invisible_with_Pos = invisibleWatermark_with_Pos(base_image,
                                                 watermark_path, (0, 0), ratio=0.2)
    invisibleWatermarked = invisibleWatermark(base_image, watermark_path)
    #extract_visibleWatermark(base_image,visibleWatermarked,alpha=0.2)
    extract_invisilbeWatermark(base_image, invisibleWatermarked)
    extract_visibleWatermark(base_image, visible_with_Pos, alpha = 0.5)
    extract_invisilbeWatermark(base_image, invisible_with_Pos)
if __name__ == '__main__':
    main()