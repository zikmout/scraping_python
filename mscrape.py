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
    print(textwrap.dedent(desc))
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='Lists collected actors/actress ...')
    parser.add_argument('--process')
    args = parser.parse_args()
    parser = argparse.ArgumentParser(
            prog='MPARSE',
            epilog='''The idea is to collect faces from famous personalities from the IMDB Database.''',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=textwrap.dedent(desc))
    #parser.print_help()

    #print("Option chosen was: %s" % args[0])

if __name__ == '__main__':
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
