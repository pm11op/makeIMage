#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
import os
from os import path

import Image
import logging

DATA_PATH = path.join(path.dirname(path.abspath(__file__)), 'data')
DL_PATH = path.join(DATA_PATH, 'org')
THUMB_SIZE = (750,348)


class ResizeImg():
    def __init__(self):
        self.files = os.listdir(DL_PATH)
        self.imgPath = path.join(DATA_PATH, str(THUMB_SIZE[0]) + 'x' + str(THUMB_SIZE[1]))
        self.mkDir()

    def resizeImg(self, filename, output):
        im = Image.open(filename)

        if im.size[0] < THUMB_SIZE[0] or im.size[1] < THUMB_SIZE[1]:
            logging.info('original file %s is less than expected', filename);
            return

        x = float(im.size[0]) / float(THUMB_SIZE[0]) if float(im.size[0] / THUMB_SIZE[0]) < float(im.size[1] / THUMB_SIZE[1]) else float(im.size[1]) / float(THUMB_SIZE[1])
        im.thumbnail((int(im.size[0]/x), int(im.size[1]/x)))
        region=im.crop((0, 0, THUMB_SIZE[0], THUMB_SIZE[1]))

        region.save(output)
        return

    def mkDir(self):
        if not path.exists(self.imgPath):
            os.mkdir(self.imgPath)

    def execute(self):
        for i, filename in enumerate(self.files):
            input = path.join(DL_PATH, filename)
            num = len(os.listdir(self.imgPath))
            output = path.join(self.imgPath, str(num+1) +'.jpg')
            print input, output
            self.resizeImg(input, output)



def main():
    resize = ResizeImg()
    resize.execute()
#    crawl.mkDir()
#    crawl.resizeImg(path.join(DL_PATH,  '24.jpg'), path.join(crawl.imgPath,  '24_s.jpg'))

 
if __name__ == "__main__":
  main()

