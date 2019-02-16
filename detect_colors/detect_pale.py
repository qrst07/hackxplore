import numpy as np
import argparse
import cv2

#to run in terminal 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# color list of boundaries
boundaries = [
	([17, 15, 100], [50, 56, 200])
]

# loop over the boundaries
for (lower, upper) in boundaries:
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
 
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
 
#uncomment following line if you want to see the image
	# cv2.imshow("images", np.hstack([image, output]))

#the following lines will write a file with the colours outlined above
	cv2.imwrite( "./output_files/nails_pale.jpg", np.hstack([output]))
	cv2.waitKey(0)
