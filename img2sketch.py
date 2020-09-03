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

import pyfiglet
import argparse

from WebApp.ImgSketch.core.ImageToSketch import Image2Sketch

DESCRIPTION = """A python script which 
            converts your favourite image to sketch like image"""


parser = argparse.ArgumentParser(
    prog="Image 2 Sketch", description=DESCRIPTION)

parser.add_argument("--inimg", "-in", type=str,
                    required=True, help="Input image path")
parser.add_argument("--ksize", "-k", type=int, default=101, help="Kernel size")
parser.add_argument("--sigma", "-s", type=float,
                    default=30.0, help="standard diviation")
parser.add_argument("--imname", "-n", type=str,
                    default="result", help="name of the out image")
parser.add_argument("--outimg", "-o", type=str,
                    default="results/", help="output image path")

args = parser.parse_args()


def printInfo():
    print("[info] Kernel size:{}".format(args.ksize))
    print("[info] Singma:{}".format(args.sigma))
    print("[info] Sketching your image....")


def printHeading(heading: str):
    statement = pyfiglet.figlet_format(heading, font="slant")
    print(statement)


def main():
    printHeading("Image 2 sketch")
    printInfo()

    im2sk = Image2Sketch(pathIn=args.inimg, pathOut=args.outimg,
                        nameOut=args.imname)
    im2sk.set_kernelsize_sigma(k=args.ksize, s=args.sigma)
    success = im2sk.sketch_it()

    if success:
        print("Image converted successfully!!")
        print("Image saved in at {}".format(args.outimg))
    else:
        print("something went wrong!")


main()
