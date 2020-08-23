'''
author: Tauhid
date : 23/08/2020
copyright (C) 2020 Tauhid, All rights reserved
'''
import numpy as np
from numpy import ndarray
from scipy.signal import convolve2d
from PIL import Image, UnidentifiedImageError


class ImageProcess:
    '''
    Main class for implementing some Image processing and image minipulation

    Algorithm implemented:
            TODO to implement Average and Lens Blurr
            -Image blur/smooth
                +Gaussian blur/smooth
                +Average blurr
                +lens blurr
            TODO to implement image resizing
            -Image Resize
                +Bicubic
                +Bilinear
            -Image converting to Grayscale
            -Image inverting
            -Image Blendding
                +color dodge
            -Image Padding
    '''

    def __init__(self):
        pass

    def _loadImage(self, path: str) -> ndarray:
        """
        reads the image from the path and returns a numpy array

        args:
            [path] - str

        returns:
            [img] numpy.ndarray with shape [h,w,c](for RGB channels) 
            or (h,w,1)(for grayscale image)
        """
        try:
            self.img = np.asarray(Image.open(path))

        except FileNotFoundError:

            print("NO such File {}".format(path))

        return self.img

    def _rotate_image_90(self, img: ndarray, k: int) -> ndarray:
        """
        Rotates the image if the img.shape[0]<img.shape[1] i.e height is less than width
        as PIL.Image.open() reads image the as [h,w,c]

        args:
            [img] - an image of type np.ndarray
            [k] - Integer to define the number of time to rotate image 90 degree i.e k*90 degree

        returns:
            [img] an rotated image of type np.ndarray
        """
        if img.shape[0] < img.shape[1]:
            self.y = np.rot90(img, k)
            return self.y
        else:
            self.img = img
            return self.img
