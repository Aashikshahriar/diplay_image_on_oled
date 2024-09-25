import cv2 as cv
import numpy as np


image_path='arduino_logo.jpg'
image=cv.imread(image_path,0)

image=cv.resize(image,(128,64)) #for 0.96 inch change it to 32

_,binary_image=cv.threshold(image,128,255,cv.THRESH_BINARY)

cv.imshow("Binary Image", binary_image)
cv.waitKey(0)
cv.destroyAllWindows()

binary_image = binary_image // 255  # Convert image to 0 and 1
binary_image = binary_image.flatten()

byte_array = [] 
for i in range(0,len(binary_image),8):
    byte=0
    for bit in range(8):
     byte|=(binary_image[i+bit]&1)<<(7-bit)
    byte_array.append(byte)


hex_array = [f"0x{byte:02X}" for byte in byte_array]
print(', '.join(hex_array))

with open('bitmap_hex_array.txt', 'w') as file:
    file.write(', '.join(hex_array))

print("Hexadecimal array saved to bitmap_hex_array.txt")