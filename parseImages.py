from PIL import Image
from bs4 import BeautifulSoup
import urllib
import urllib2
import cStringIO
import re

YELLOW = (264, 264, 0)
GREY = (64, 64, 64)

url = """http://algdb.net/Set/OLL"""

file = urllib2.urlopen(url)
soup = BeautifulSoup(file, 'html.parser')

table = soup.find("table")

for row in table.find_all("tr"):
    data = row.find_all("td")
    if len(data) ==0:
        continue

    match = re.search(r"""OLL (\d+)""", data[0].string)
    if match:
        print match.group(1)

        imgurl = data[1].img['src']
        imgurl = urllib.quote(imgurl, safe="%/:=&?~#+!$,;'@()*[]")
        print imgurl

        file = cStringIO.StringIO(urllib2.urlopen(imgurl).read())
        img = Image.open(file)
        img.show()
        img.save("img1.png", "png")
        print "after show"
        exit()