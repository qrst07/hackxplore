#import nails_yellow file:

# count the number of non-black pixels
# (non-black pixels / total pixels) * 100 = percentage of nail
# output

#import nails_blue file:
# count the number of non-black pixels

#import nails_pale file:
# count the number of non-black pixels

from PIL import Image
im = Image.open('./output_files/nails_yellow.jpg')

non_black = 0
black = 0
boundaries = [
	([153, 213, 244], [218, 246, 249])
]

for pixel in im.getdata():
    if (pixel == (0,0,0)): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        black += 1
    else:
        non_black += 1

percentage = (black / (black+non_black))*100

print(f"Number of black pixels: {black}. The percentage of black is {percentage}")