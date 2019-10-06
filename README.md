# Convert grayscale to RGB & RGB to grayscale

1) Covert image from RGB to grayscale 
2) Convert image from grayscale to RBG
writen in python.


## Features

![](https://github.com/israelDuani/python-grayscale-to-color/blob/master/ReadmeFiles/ColorToGray.PNG)

![](https://github.com/israelDuani/python-grayscale-to-color/blob/master/ReadmeFiles/GrayToColor.PNG)



### Requirements

  * Python 2.7
  * Pillow
  * Matplotlib
  * Numpy

## Usage

### CMD

You can use 2 scripts

* `ColorToGray.py` - Covert image from RGB to grayscale.
* `GrayToColor.py` - Convert image from grayscale to RBG.

#### ColorToGray.py

To use this script open cmd in the same folder that the script located and run this command:

```cmd
python ColorToGray.py yourImageName.png
```
the output will be a saved image in the same folder that the script located.
the new image name will be  youImageNameGray.png

#### GrayToColor.py

To use this script open cmd in the same folder that the script located and run this command:

```cmd
python GrayToColor.py yourImageName.png
```
the output will be a saved image in the same folder that the script located.
the new image name will be  youImageNameColor.png


### Attention

This python script can convert from grayscale to RGB only if the grayscale image created by "ColorToGray.py" script
