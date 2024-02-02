import numpy as np
import argparse
import cv2

#argparse 
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", help = "path to the image")
args = vars(parser.parse_args())

#load the image 
image = cv2.imread(args["image"])

# #define the list of color boundaries
# #colors are in GRB format
# boundaries = [
# 	([17, 15, 100], [50, 56, 200]),
# 	([86, 31, 4], [220, 88, 50]),
# 	([25, 146, 190], [62, 174, 250]),
# 	([103, 86, 65], [145, 133, 128])
# ]

# for (lower, upper) in boundaries:
# 	# create NumPy arrays from the boundaries
# 	lower = np.array(lower, dtype = "uint8")
# 	upper = np.array(upper, dtype = "uint8")
# 	# find the colors within the specified boundaries and apply
# 	# the mask
# 	mask = cv2.inRange(image, lower, upper)
# 	output = cv2.bitwise_and(image, image, mask = mask)
# 	# show the images
# 	cv2.imshow("images", np.hstack([image, output]))
# 	cv2.waitKey(0)

color_boundaries = {
    "red":    ([0,   0,   255], [127, 0,   255]),
    "blue":   ([255, 38,  0],   [255, 38,  0]),
    "yellow": ([0,   216, 255], [0,   216, 255]),
    "grey":   ([160, 160, 160], [160, 160, 160])
}

for color_name, (lower, upper) in color_boundaries.items():
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = np.uint8)
    upper = np.array(upper, dtype = np.uint8)

    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    if mask.any():
        print("Object detected as: ", f"{color_name}")