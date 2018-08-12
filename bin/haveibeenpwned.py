#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, argparse
from haveibeenpwned.status import pwned, pwned_full
from haveibeenpwned import __version__, __summary__


def _display_status(email):
    if pwned(email):
        print('This email address has been pwned!')
    else:
        print('No problems here! :-)')
        print('More detailed data on: https://haveibeenpwned.com/')


def _display_status_with_data(email):
    response = pwned_full(email)
    if not response:
        print('No problems here! :-)')
    else:
        print(response)
        print('More detailed data on: https://haveibeenpwned.com/')


def main():
    parser = argparse.ArgumentParser(description=__summary__)
    parser.add_argument('-v', '--version', action='store_true', help='currently installed version')
    parser.add_argument('-r', '--full', action='store_true', help='response will full data not just boolean, if any exists')
    args = parser.parse_args()
    email = None
    if args.full:
        _display_status_with_data(email)
    if args.version:
        print(__version__)
        sys.exit(1)

    _display_status(email)


if __name__ == '__main__':
    main()
