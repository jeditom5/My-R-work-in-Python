#!/usr/bin/python3

from PIL import Image
import os, glob, subprocess, re

SIZE = 128, 128
ANGLE = 270
def fixImages():
    for image in glob.glob('./images/*'):
        index = len('./images/')
        new_image = open('/opt/icons/'+image[index:], 'wb')
        with Image.open(image) as im:
             imm = im.rotate(ANGLE).resize(SIZE)
             imm.mode = 'L'
             imm.save(new_image, format='JPEG')
        new_image.close()
def main():
    fixImages()
if __name__ == "__main__":
    main()