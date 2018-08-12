#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse
from haveibeenpwned.status import check
from haveibeenpwned import __version__, __summary__


def _display_status():
    print('displaying data here')


def _display_status_with_data():
    print('test')


def main():
    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument('-v', '--version', action='store_true', help='currently installed version')
    parser.add_argument('-r', '--full', action='store_true', help='response will full data not just boolean, if any exists')
    args = parser.parse_args()
    if args.full:
        _display_status_with_data()
    if args.version:
        print(__version__)
        sys.exit(1)

    _display_status()


if __name__ == '__main__':
    main()
