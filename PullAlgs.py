from bs4 import BeautifulSoup
import urllib2

url = "http://cubewhiz.com/oll.php"

file = urllib2.urlopen(url)
soup = BeautifulSoup(file, 'html.parser')

for table in soup.find_all("table"):
    for row in table.find_all("tr"):
        if row.b:
            print row.find("b").string