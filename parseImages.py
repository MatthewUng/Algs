from PIL import Image
from bs4 import BeautifulSoup
import urllib
import urllib2
import cStringIO
import re
from rotation import *


YELLOW = (254, 254, 0, 255)
GREY = (64, 64, 64, 255)


def parse_image(im):
    # edges
    out = [[0, 0, 0] for _ in range(3)]

    # upper left
    if im.getpixel((30,30)) == YELLOW:
        out[0][0] = 0
    elif im.getpixel((15, 30)) == YELLOW:
        out[0][0] = 1
    else:
        out[0][0] = 2

    # upper middle
    if im.getpixel((50, 30)) == YELLOW:
        out[1][0] = 0
    else:
        out[1][0] = 1

    # upper right
    if im.getpixel((70, 30)) == YELLOW:
        out[2][0] = 0
    elif im.getpixel((70, 15)) == YELLOW:
        out[2][0] = 1
    else:
        out[2][0] = 2

    # middle left
    if im.getpixel((30, 50)) == YELLOW:
        out[0][1] = 0
    else:
        out[0][1] = 1

    # middle right
    if im.getpixel((70, 50)) == YELLOW:
        out[2][1] = 0
    else:
        out[2][1] = 1

    # lower left
    if im.getpixel((30, 70)) == YELLOW:
        out[0][2] = 0
    elif im.getpixel((30, 85)) == YELLOW:
        out[0][2] = 1
    else:
        out[0][2] = 2

    # lower middle
    if im.getpixel((50, 70)) == YELLOW:
        out[1][2] = 0
    else:
        out[1][2] = 1

    # lower right
    if im.getpixel((70, 70)) == YELLOW:
        out[2][2] = 0
    elif im.getpixel((85, 70)) == YELLOW:
        out[2][2] = 1
    else:
        out[2][2] = 2

    return out




url = """http://algdb.net/Set/OLL"""

file = urllib2.urlopen(url)
soup = BeautifulSoup(file, 'html.parser')

table = soup.find("table")

hash = dict()
for row in table.find_all("tr"):
    data = row.find_all("td")
    if len(data) ==0:
        continue

    match = re.search(r"""OLL (\d+)""", data[0].string)
    if match:
        print match.group(1)
        imgurl = data[1].img['src']
        imgurl = urllib.quote(imgurl, safe="%/:=&?~#+!$,;'@()*[]")

        img_file = cStringIO.StringIO(urllib2.urlopen(imgurl).read())
        img = Image.open(img_file)


        pattern = parse_image(img)
        print "hashing..."
        for thing in rotations(pattern):
            print thing
            hash[thing] = int(match.group(1))



with open("orientation_data.p", "wb") as FILE:
    pickle.dump(hash, FILE, protocol=pickle.HIGHEST_PROTOCOL)

FILE.close()