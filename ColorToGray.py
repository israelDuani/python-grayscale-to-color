from PIL import Image
import matplotlib.pyplot as plt
import math
import numpy as np
import sys

# get the image to process as argument
imageFullName = sys.argv[1]
imageArg = imageFullName.split('.')
imageName = imageArg[0]

# load the image
colorImage = Image.open(imageFullName)
pixelArr = colorImage.load()

# get the width and height of the image
imgWidth = colorImage.size[0]  
imgHight = colorImage.size[1]

# create array of grayscale for the new image
grayArr = np.zeros((imgHight, imgWidth,3), dtype=np.uint8)

# process every pixel in the image
for h in range(0,imgHight):
    for w in range(0,imgWidth):
        # calculate the grayscale values
        redVal = int(pixelArr[w,h][0]*0.21)
        greenVal = int(pixelArr[w,h][1]*0.72)
        blueVal = int(pixelArr[w,h][2]*0.07)
        grayVal = int(round(redVal + greenVal + blueVal))

        # encrypt the RBG colors in the grayscale value
        red = int(math.sqrt(round(pixelArr[w,h][0])))
        blue = int(math.sqrt(round(pixelArr[w,h][2])))

        # handle extream case
        if(red+grayVal > 255):
            grayVal = 255 - red
        if(blue+grayVal > 255):
            grayVal = 255 - blue

        # put the RGB values in the new image array 
        grayArr[h][w] = (grayVal+red,grayVal,grayVal+blue)

# save the new image
grayImg = Image.fromarray(grayArr, 'RGB')            
grayImg.save(imageName + "Gray" + ".png")
