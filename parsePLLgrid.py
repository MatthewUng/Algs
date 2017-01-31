from PIL import Image
from bs4 import BeautifulSoup
import urllib
import urllib2
import cStringIO
import cPickle as pickle
import re
from rotation import *

BLUE = [0, 0, 242]
RED = [238, 0, 0]
ORANGE = [255, 161, 0]
GREEN = [0, 216, 0]

def getColor(r,g,b,x):
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

def save(d, fname):
    with open(fname, "wb") as f:
        pickle.dump(d, f, protocol=pickle.HIGHEST_PROTOCOL)

class PLLimageParser:
    site_url = "http://algdb.net/Set/PLL"

    def __init__(self):
        pass

    def createAlgs(self, algs):
        d = dict()
        for alg in algs:
            #print alg
            name = alg[0].string
            alg_str = alg[2].renderContents()
            print alg[0].string
            print alg[2].renderContents()
            d[name] = alg_str
        save(d, "algorithms_PLL.p")


    def createStandard(self, algs):
        d = dict()
        for alg in algs:
            name = alg[0].string
            img_url = alg[1].img['src']
            img_url = urllib.quote(img_url, safe="%/:=&?~#+!$,;'@()*[]")
            img_file = cStringIO.StringIO(urllib2.urlopen(img_url).read())
            img = Image.open(img_file)

            pattern = self.parse(img)
            print name
            for line in pattern:
                print line
            d[name] = pattern
        save(d, "standard_PLL.p")

    def AlgData(self):
        file = urllib2.urlopen(PLLimageParser.site_url)
        soup = BeautifulSoup(file, 'html.parser')

        out = list()
        table = soup.find("table")
        for row in table.find_all("tr"):
            data = row.find_all("td")
            if len(data)>0:
                out.append(data)
        return out

    def parse(self, im):
        out = [[None for _ in range(3)] for _ in range(3)]

        # edges
        edges = {(1,0):(15,50),
                 (0,1):(50,15),
                 (2,1):(50,85),
                 (1,2):(85,50)}
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

        corners = {(0,0) : (15,30),
                   (2,0) : (30,85),
                   (0,2) : (70,15),
                   (2,2) : (85,70)}
        for index, pixel in corners.items():
            color = getColor(*im.getpixel(pixel))
            if color:
                out[index[0]][index[1]] = color_map[color]
            else:
                print "error in parse()"
                raise Exception
        return out


if __name__ == "__main__":
    parser = PLLimageParser()
    algs = parser.AlgData()
    parser.createAlgs(algs)


