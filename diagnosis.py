#import nails_yellow file:

# count the number of non-black pixels
# (non-black pixels / total pixels) * 100 = percentage of nail
# output

#import nails_blue file:
# count the number of non-black pixels

#import nails_pale file:
# count the number of non-black pixels

from PIL import Image
import matplotlib.pyplot as plt

# YELLOW 

im = Image.open('./output_files/nails_yellow.jpg')

yellow = 0
black1 = 0
boundaries = [
	([153, 213, 244], [218, 246, 249])
]

for pixel in im.getdata():
    if (pixel == (0,0,0)): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        black1 += 1
    else:
        yellow += 1

percentage1 = (black1 / (black1+yellow))*100

percentage_yellow = 100 - percentage

# PALE

im = Image.open('./output_files/nails_pale.jpg')

pale = 0
black2 = 0
boundaries = [
	([153, 213, 244], [218, 246, 249])
]

for pixel in im.getdata():
    if (pixel == (0,0,0)): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        black2 += 1
    else:
        pale += 1

percentage2 = (black2 / (black2+pale))*100

percentage_pale = 100 - percentage

# BLUE

im = Image.open('./output_files/nails_blue.jpg')

blue = 0
black3 = 0
boundaries = [
	([153, 213, 244], [218, 246, 249])
]

for pixel in im.getdata():
    if (pixel == (0,0,0)): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        black3 += 1
    else:
        blue += 1

percentage3 = (black3 / (black3+blue))*100

percentage_blue = 100 - percentage

# OUTPUT CHART

labels = 'Signs of fungal infection', 'Signs of anemia', 'Signs of low oxygen levels', 'Healthy nail'
sizes = [percentage_yellow, percentage_pale, percentage_blue, black]
colors = ['yellow', 'white', 'blue', 'pink']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.show()

# OUTPUT DIAGNOSIS

if (percentage_yellow >= 0 || percentage_pale >= 0 || percentage_blue >= 0):
    print ("You show signs of the above diseases - we recommend that you go to a partner physician near you!")
else:
    print ("Your nails indicate you are healthy! If you have concerns, be sure to still see a physician near you!")