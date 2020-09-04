"""
BSD 3-Clause License

Copyright (c) 2020, Tauhid Khan, Devyesh Thomas
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import numpy as np
from numpy import ndarray
from PIL import Image

from datetime import datetime

#from WebApp.ImgSketch.core.ProcessImage import ImageProcess
from .ProcessImage import ImageProcess


class Image2Sketch(ImageProcess):
    """
    A Class to convert an image to sketch like image

    Constructor args:
        pathIn - [str] Path to input image
        pathOut - [str] path to output image
        nameOut - [str] name of the output image
        kernel_size - [int] size of the gaussian kernel for blurring
        sigma - [float] standard deviation for gaussian distribution
    """

    def __init__(self, pathIn: str, pathOut: str, nameOut: str, kernel_size: int = 21, sigma: float = 10.0):
        super().__init__()
        self.__KERNEL_SIZE = kernel_size
        self.__SIGMA = sigma
        self.__pathIn = pathIn
        self.__pathOut = pathOut
        self.__nameOut = nameOut
        self.succes = False

    # getter setters
    def get_kernel_size(self) -> int:
        return self.__KERNEL_SIZE

    def get_sigma(self) -> float:
        return self.__SIGMA

    def set_kernelsize_sigma(self, k: int, s: int):
        self.__KERNEL_SIZE = k
        self.__SIGMA = s

    # helper functions

    def _adjust_height_width(self, img: ndarray):
        """
        TODO Adjust the height and width(mainly downsample the image to speed up calculation)
        """
        pass

    # main function
    def sketch_it(self) -> bool:
        """
        TODO Add full docstring here
        """
        self.originalImg = super().loadImage(self.__pathIn)

        self.grayImg = super().RGB2GRAY(self.originalImg)
        self.negativeImg = super().invertImage(self.grayImg)
        self.negativeBlur = super().gaussianBlur(
            img=self.negativeImg,
            kernel_size=self.__KERNEL_SIZE,
            sigma=self.__SIGMA)

        # normalize gray image and negative blur in order to blend
        self.grayImg = super()._normalize_img(self.grayImg)
        self.negativeBlur = super()._normalize_img(self.negativeBlur)
        self.sketchImg = super().colorDodge(
            img1=self.negativeBlur,
            img2=self.grayImg)
        self.succes = super().saveImage(self.sketchImg, self.__pathOut,
                                        "sketched_"+self.__nameOut)
        return self.succes

    def __str__(self):
        return """
        A Class to convert an image to sketch like image

        Constructor args:
            pathIn - [str] Path to input image
            pathOut - [str] path to output image
            nameOut - [str] name of the output image
            kernel_size - [int] size of the gaussian kernel for blurring
            sigma - [float] standard deviation for gaussian distribution
        """

