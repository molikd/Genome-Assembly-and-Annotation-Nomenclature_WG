import argparse
import textwrap
import sys
import re

def main():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Validate a GAAN name',
            epilog=textwrap.dedent('''\
                        input must be:
                            <input> - a GAAN assembly name 
                            '''))

    parser.add_argument('ascii', 
            nargs=1,
                        metavar='TODO.EXAMPLE',
            help='input, name to be validated')

    parser.add_argument('--version', action='version', version='%(prog)s 0.0.1')
