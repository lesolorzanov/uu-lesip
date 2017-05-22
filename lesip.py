"""Image processing tools module.

This module contains definitions and classes to create a library for
all image processing needs in the several undergoing projects for the
Center for Image Analysis, Uppsala University.

Import:
    To import simply add
        $ import lesip
    to your python code. All has been created as a module for this
    exercise.


"""

import scipy.misc
import numpy as np

class ImageProcessor:
    """
    This class containts several methods that are needed to apply image
    filters. In this case only downsampling is implemented.

    :param name: path and file of the image to process
    :param mode: black and white or RGB
    :type name: string
    :type mode: string

    This class uses SciPy which uses PIL to load images, possible modes are:
        * 'L' (8-bit pixels, black and white)
        * 'P' (8-bit pixels, mapped to any other mode using a color palette)
        * 'RGB' (3x8-bit pixels, true color)
        * 'RGBA' (4x8-bit pixels, true color with transparency mask)
        * 'CMYK' (4x8-bit pixels, color separation)
        * 'YCbCr' (3x8-bit pixels, color video format)
        * 'I' (32-bit signed integer pixels)
        * 'F' (32-bit floating point pixels)

    """
    def __init__(self,name='',mode='L'):
        self.name=name
        self.mode=mode
        self.status=0
        self.image=None

    """
    I created this function as a vestige of my use of private and public variables
    """
    def setName(name):
        self.name=name

    """
    I created this function as a vestige of my use of private and public variables
    """
    def setMode(mode):
        self.mode=mode

    """
    Uses Scipy to load the image into an array to process. The image name must
    be set before either at construction or afterwards.

    """
    def loadImage(self):
        self.image=scipy.misc.imread(self.name)
        status=1

    """
    Uses reshape to make binning easier. It has to be cropped to fit the bin size
    reshaped to 4D and then the function used to select the intensity. This cases
    is maximum because the information should be preserved accross resolutions.

    A binning factor is given, default is 2

    :param factor: Factor for resampling
    :type factor: int
    """
    def binning(self,factor=2):
        #remove remaining pixels
        w, h=self.image.shape
        self.image=self.image[0:w-w%factor,0:h-h%factor]
        self.image=self.image.reshape(w//factor,factor,h//factor,factor)
        self.image=self.image.max(axis=3).sum(axis=1)

    """
    Uses scipy to save the image, a file name and path must be given

    """
    def saveImage(self,name):
        scipy.misc.imsave(name, self.image)
