from bs4 import BeautifulSoup
import urllib2
import re
import cPickle as pickle

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

hash = dict()
for row in soup.find("table").find_all("tr"):
    data = row.find_all("td")

    if len(data) < 3:
        continue
    match = re.match(r'OLL (\d+)', data[0].string)
    if match:
        index = int(match.group(1))
        print data[0].get_text()
        l = data[2].get_text().split("\r\n")
        l = [x.encode("ascii", "ignore") for x in l[1:]]
        l = map(str.strip, l)

        s = '\n'.join(l)
        hash[index] = l
        print s
exit()
with open("OLL_algorithm_data.p", 'wb') as FILE:
    pickle.dump(hash, FILE, pickle.HIGHEST_PROTOCOL)


