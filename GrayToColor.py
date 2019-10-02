from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import sys

# get the image to process as argument
imageFullName = sys.argv[1]
imageArg = imageFullName.split('.')
imageName = imageArg[0]
imageFormat = '.' + imageArg[1]

# load the image
grayImage = Image.open(imageFullName)
pixelArr = grayImage.load()

# get the width and height of the image
imgWidth = grayImage.size[0]  
imgHight = grayImage.size[1]

# create array of RGB color for the new image
colorArr = np.zeros((imgHight, imgWidth, 3), dtype=np.uint8)

# process every pixel in the image
for h in range(0,imgHight):
    for w in range(0,imgWidth):
        # calculate the RGB values
        red = int((int(pixelArr[w,h][0] - pixelArr[w,h][1])**2)) 
        blue = int((int(pixelArr[w,h][2] - pixelArr[w,h][1])**2)) 
        green = int(round((pixelArr[w,h][1] - red*0.21 - blue*0.07)/0.72))
            
        # handle extream case
        if green > 255:
            green = 255
        if green < 0:
            green = 0
            
        # put the RGB values in the new image array
        colorArr[h][w] = (red,green,blue)
        
# save the new image
colorImg = Image.fromarray(colorArr, 'RGB')            
colorImg.save(imageName + "Color" + ".png")#imageFormat)


