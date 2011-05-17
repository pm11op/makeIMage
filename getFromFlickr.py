#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
import os
from os import path

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup

DATA_PATH = path.join(path.dirname(path.abspath(__file__)), 'data')
DL_PATH = path.join(DATA_PATH, 'org')


class ImgFlickr():
    def __init__(self):
        self.url = 'http://api.flickr.com/services/feeds/photos_public.gne?tags=flower'
        files = os.listdir(DL_PATH)
        self.num = len(files)

   
    def getHTML(self):
        opener = urllib2.build_opener()
        html = opener.open(self.url).read()
        return html
        
    def parseImgs(self, html):
        soup = BeautifulSoup(html)
        links = soup.findAll(rel="enclosure")
        for i,url in enumerate(links):
            filename = path.join(DL_PATH, str(i + self.num) +'.jpg')
            print filename
            urllib.urlretrieve(url['href'], filename)


                                 

def main():
    crawl = ImgFlickr()
    html = crawl.getHTML()
    crawl.parseImgs(html)
 
if __name__ == "__main__":
  main()

