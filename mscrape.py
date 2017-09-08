import sys
import argparse
from sys import argv
import textwrap
import os

from urllib.request import urlretrieve
from urllib.request import urlopen

import urllib
import urllib.request as urllib2

from bs4 import BeautifulSoup
import json

def main(argv):


    def nbArtistes(path):
        count = 0
        for k in os.listdir(path):
            print(k, "\n")
            count = count + 1
        return count

    def get_soup(url, header):
        return BeautifulSoup(urlopen(urllib2.Request(url, headers=header)), 'html.parser')

    desc = '''\
    <     Important information     >
    ---------------------------------
    This software is meant to be used
    on research purpose only.
    ---------------------------------
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--process', help='Counts the number and process the celebrities')
    parser.add_argument('-q', '--query', default='bananas', type=str, help='picture you are looking for')
    parser.add_argument('-b', '--verbose', help='verbose mode.', action='store_true')
    parser.add_argument('-n', '--nb_images', help='how many images per request')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0',
            help='prints out the version.')
    args = parser.parse_args()
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent(desc))
    parser.print_help()

    print("\n###### Listing files ... #####\n")
    print("Numbers of artists reported: " , nbArtistes(args.process))
    print("Option chosen was: %s" % args)
    print ("\nYou chose the following folder: \n", args.process)
    print ("\nYou want to query: \n", args.query)
    print("And you want ", args.nb_images)
    #https://www.google.co.in/search?q=%22paul%20henreid%22&source=lnms&tbm=isch#imgrc=_
    # Begining scraping phase

    query = args.query
    query = query.split()
    query = '+'.join(query)
    url = 'https://www.google.co.in/search?q=%22'+query+'%22&source=lnms&tbm=isch#imgrc=_'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.13 Safari/537.36'}
    soup = get_soup(url, header)
    ActualImages=[]
    for a in soup.find_all("div", {"class":"rg_meta"}):
        link, Type = json.loads(a.text)['ou'], json.loads(a.text)['ity']
        ActualImages.append((link, Type))
        #log
        #print(ActualImages)


    #urlretrieve(imageLocation)

if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
