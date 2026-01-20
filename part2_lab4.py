#!/usr/bin/python3
import os, glob, requests

url = "http://localhost/upload/"
def images_upload():
  for image in glob.glob(os.getcwd()+'/supplier-data/images/*.jpeg'):
    with open(image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})

if __name__ == "__main__":

    images_upload()