#!/usr/bin/python3

from PIL import Image
import glob, os

SIZE = 600, 400
def fixImages():
    for image in glob.glob(os.getcwd()+'/supplier-data/images/*.tiff'):
        file, ext = os.path.splitext(image)
        new_image = open(file+'.jpeg', 'wb')
        with Image.open(image) as im:
             imm = im.convert('RGB').resize(SIZE)
             imm.mode = 'L'
             imm.save(new_image, format='JPEG')
        new_image.close()
def main():
    fixImages()
if __name__ == "__main__":
    main()