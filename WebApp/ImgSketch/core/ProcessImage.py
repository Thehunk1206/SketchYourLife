'''
author: Tauhid
date : 23/08/2020
copyright (C) 2020 Tauhid, All rights reserved
'''
import numpy as np
from numpy import ndarray
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

    # Some utils functions

    def _rotate_image_90(self, img: ndarray, k: int) -> ndarray:
        """
        TODO to implement image rotation without using np.rot90()

        Rotates the image if the img.shape[0]<img.shape[1] 
        i.e height is less than width as PIL.Image.open() 
        reads image the as [h,w,c]

        args:
            img - [ndarray] an image of type np.ndarray
            k - [int] Integer to define the number of time 
                to rotate image 90 degree i.e k*90 degree

        returns:
            img - [ndarray] an rotated image of type np.ndarray
        """
        if img.shape[0] < img.shape[1]:
            self.y = np.rot90(img, k)
            return self.y
        else:
            self.img = img
            return self.img

    def _gaussian_distribution(self, x: ndarray, mu: float, sigma: float) -> ndarray:
        """
        It returns the gassian distribution of the given ndarray

        args:
            [x] - [ndarray] 
            mu - [float] mean of the gaussian distribution
            sigma - [float] standard deviation of the gaussian distribution

        return:
            ndarray - Gaussian distribution of the given x ndarray with
            standard deviation sigma and mean mu
        """
        return 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(
            -np.power(
                (x - mu) / sigma, 2) / 2)

    def _generate_gaussian_kernel(self, size: int, sigma: float = 1.0, mu: float = 0.0) -> ndarray:
        """
        Generate gaussian kernel of given given size and dims (sizexsize)

        args:
            size - [int] deifnes the size of the kernel (sizexsize)
            sigma - [float] standard diviation of gaussian
                    distribution. It cannot be 0.0
            mu - [float] mean of the gaussian distribution

        return:
            kernel2D - [ndarray] gaussian kernel the values are in range (0,1)
        """
        # create the 1D array of equally spaced distance point of given size
        self.kernel_1d = np.linspace(-(size//2), size//2, size)
        # get the gaussian distribution of the 1D array
        self.kernel_1d = _gaussian_distribution(kernel_1d, mu, sigma)

        # Compute the outer product of kernel1D tranpose and kernel1D
        self.kernel_2d = np.outer(self.kernel_1d.T, self.kernel_1d)
        # normalize the the outer product to suish the values between 0.0-1.0
        self.kernel_2d *= 1.0/self.kernel_2d.max()
        return self.kernel_2d

    def _pad_image(self, img: ndarray, pad_width: int = 10) -> ndarray:
        """
        TODO to implement padding for RGB images.

        NOTE: Currently it can pad only grayscale image only

        Pads the image from all side with zeros.

        args:
            img - [ndarray] image to padded
            pad_width - [int] width of the pad around the image

        return:
            padded_img - [ndarray] image with padding around
        """
        self.padded_img = np.zeros(
            (img.shape[0] + pad_width*2, img.shape[1]+pad_width*2))
        self.padded_img[pad_width:-pad_width, pad_width:-pad_width] = img
        return self.padded_img

    def _normalize_img(self, img: ndarray, range_end: float = 1.0) -> ndarray:
        """
        NOTE: range should be > 0.0

        Normalize the image pixel values in range (0,range_range).

        args:
            img - [ndarray] input image to be normalized.
            range_end -[float] 

        return:
            img - [ndarray] normalized image
        """
        return (img/img.max())*range_end

    def _isGrayscale(self, img: ndarray) -> bool:
        """
        Checks if image is grayscale or not

        arg:
            img - [ndarray] image to check

        return
            bool 
        """
        if len(np.squeeze(img).shape) == 2:
            return True
        else:
            return False
    # main functions

    def loadImage(self, path: str) -> ndarray:
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
            return None
        return self.img

    def RGB2GRAY(self, img: ndarray) -> ndarray:
        """
        Converts a RGB image to Grayscale image

        args:
            img - [ndarray] image that to be converted to grayscale

        return:
            img - [ndarray] Converted grayscale image

        """
        # checks if the image is already in grayscale format
        if _isGrayscale(img):
            return img
        else:
            self.rgb_weights = np.array([0.2126, 0.7152, 0.0722])
            return np.dot(img[..., :3], self.rgb_weights)

    def invertImage(self, img: ndarray) -> ndarray:
        """
        Inverts an image

        args:
            img - [ndarray] image that to be inverted

        return:
            img - [ndarray] inverted image
        """
        return img.max() - img

    def naiveConvolve2D(self, img: ndarray, kernel: ndarray) -> ndarray:
        """
        TODO:to implement fater version of the convolution operatration 
            and add striding to downsample image

        NOTE:It is a naive approach to convolve image with kernel.

        Convolves image with the given kernel

        args:
            img - [ndarray] input image
            kernel - [ndarray] kernel of any size

        return:
            convolved2d - [ndarray] a convolved
        """
        self.kernel_size = kernel.shape[0]
        self.convolved_output = np.zeros_like(img)

        self.padded_image = _pad_image(img, pad_width=kernel_size-2)

        for x in range(img.shape[1]):
            for y in range(img.shape[0]):
                self.convolved_output[y, x] = (
                    kernel * self.padded_image[y:y+kernel_size, x:x+kernel_size]).sum()

        return self.convolved_output

    def colorDodge(self, img1: ndarray, img2: ndarray) -> ndarray:
        """
        TODO to implement different type of image blending
        It blends the image1 with image2 as background

        args:
            img1 - [ndarray] image 1
            img2 - [ndarray] image 2

        return:
            blended_img - [ndarray] Image1 blended with Image2
        """
        self.blended_img = img2/((1.0 - img1)+10e-12)
        self.blended_img[self.blended_img > 1.0] = 1.0
        self.blended_img = _normalize_img(self.blended_img, range_end=255.0)
        return self.blended_img
