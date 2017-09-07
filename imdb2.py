from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getName(url):
    img = 'simon'
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        name = bsObj.findAll("span", {'itemprop':'name'})
        img = bsObj.find("td", {'id': 'img_primary'}).img['src']
    except AttributeError as e:
        return None
    return name, img

name = getName('http://www.imdb.com/name/nm0000001/')
if name == None:
    print("URL NOT FOUNNNNND")
else:
    for val in name[0]:
        print(bcolors.WARNING + val.get_text() + bcolors.ENDC)
    print(bcolors.OKBLUE +  name[1])
    testfile = requests.get(name[1], allow_redirects=True)
    open(str("./imgs/" + val.get_text()) + ".jpg", 'wb').write(testfile.content)
