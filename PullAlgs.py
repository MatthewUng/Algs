from bs4 import BeautifulSoup
import urllib2

cubewhiz = "http://cubewhiz.com/oll.php"
algdb = "http://algdb.net/Set/OLL"

"""
file = urllib2.urlopen(cubewhiz)
soup = BeautifulSoup(file, 'html.parser')

for table in soup.find_all("table"):
    for row in table.find_all("tr"):
        if row.b:
            print row.find("b").string
"""

file = urllib2.urlopen(algdb)
soup = BeautifulSoup(file, "html.parser")


for row in soup.find("table").find_all("tr"):
    data = row.find_all("td")

    if len(data) < 3:
        continue
    if "OLL" in data[0].string:
        print data[0].get_text()
        print data[2].get_text()


