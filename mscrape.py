import sys
import argparse
from sys import argv
import textwrap
import os

def main(argv):
    desc = '''\
    <     Important information     >
    ---------------------------------
    This software is meant to be used
    on research purpose only.
    ---------------------------------
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--process', help='Counts the number and process the celebrities')
    parser.add_argument('-b', '--verbose', help='verbose mode.', action='store_true')
    parser.add_argument('-n', '--image_nb', help='how many images per request', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help='prints out the version.')
    args = parser.parse_args()
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent(desc))
    parser.print_help()

    print("Option chosen was: %s" % args)
    print ("\nYou shose the following folder: \n", args.process)

    #print("Home is: ", os.listdir(imgs))

if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
