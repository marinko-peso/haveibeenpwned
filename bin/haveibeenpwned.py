#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse
from haveibeenpwned.status import check
from haveibeenpwned import __version__, __summary__


def _display_data():
    print('displaying data here')


def main():
    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument('-v', '--version', action='store_true', help='currently installed version')
    parser.add_argument('-r', '--raw', action='store_true', help='raw parsed data without cli')
    args = parser.parse_args()
    # if args.raw:
    #     _display_scrapped_and_exit()
    if args.version:
        print(__version__)
        sys.exit(1)

    _display_data()


if __name__ == '__main__':
    main()
