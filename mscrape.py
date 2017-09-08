import sys
import argparse
from sys import argv
import textwrap

def main(argv):
    desc = '''\
    <     Important information     >
    ---------------------------------
    This software is meant to be used
    on research purpose only.
    ---------------------------------
    '''
    parser = argparse.ArgumentParser()
    #parser = argparse.ArgumentParser(description='Lists collected actors/actress ...')
    parser.add_argument('--process', help='Counts the number and process the celebrities')
    parser.add_argument('--verbose', help='verbose mode.', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0', help='prints out the version.')
    args = parser.parse_args()
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent(desc))
            #epilog='''The idea is to collect faces from famous personalities from the IMDB Database.''',
            #formatter_class=argparse.RawDescriptionHelpFormatter,
    parser.print_help()

    #dirname = args[0]
    #print("Option chosen was: %s" % args[0])

if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
