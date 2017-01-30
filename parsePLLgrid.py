from PIL import Image
from bs4 import BeautifulSoup
import urllib
import urllib2
import cStringIO
import re
from rotation import *

BLUE = [0, 0, 242]
RED = [238, 0, 0]
ORANGE = [255, 161, 0]
GREEN = [0, 216, 0]

def getColor(r,g,b):
    if [r,g,b] == BLUE:
        return "b"
    elif [r,g,b] == RED:
        return "r"
    elif [r,g,b] == ORANGE:
        return "o"
    elif [r,g,b] == GREEN:
        return "g"
    else:
        print "error in getColor()"


class PLLimageParser:

    def __init__(self):
        pass


    def parse(self, im):
        out = [[None for _ in range(3)] for _ in range(3)]

        # edges
        edges = {(1,0):[50,15],
                 (0,1):[15,50],
                 (2,0):[85,50],
                 (0,2):[50,85]}
        for index, pixel in edges.items():
            color = getColor(*im.getpixel(pixel))
            if color:
                out[index[0]][index[1]] = color
            else:
                print "error in parse()"
                raise Exception

        #corners
        color_map = {'r':'rb',
                     'b':'bo',
                     'g':'gr',
                     'o':'og'}

        corners = {(0,0) : [15,30],
                   (2,0) : [70, 15],
                   (0,2) : [30,85],
                   (2,2) : [85,70]}
        for index, pixel in corners.items():
            color = getColor(*im.getpixel(pixel))
            if color:
                out[index[0]][index[1]] = color
            else:
                print "error in parse()"
                raise Exception
        return out


if __name__ == "__main__":
    parser = PLLimageParser()
    im = Image.open('img2.png')

    out = parser.parse(im)
    for line in out:
        print line
