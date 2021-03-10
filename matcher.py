# -*- coding: utf-8 -*-
# Elena Kröner
# Python 3.8

import argparse
import sys

import searchalgorithm as sm


def define_argparser():
    parser = argparse.ArgumentParser(description="String Matcher")
    parser.add_argument("suche", help="Search a string in a text")
    parser.add_argument("-i", "--ignore", action="store_true",
                        help="Set to case-insensitive")
    parser.add_argument("-n", "--naive", action="store_true",
                        help="Use the naive search algorithm")
    parser.add_argument("suchbegriff", type=str,
                        help="The string you want to look for")
    parser.add_argument("text", type=str, help="String, .txt-file or folder,\
                        which will be searched")
    args = parser.parse_args()
    return args


def main():
    args = define_argparser()

    # check if string is not empty
    string = args.suchbegriff
    if not string:
        print("Bitte einen Suchbegriff der Länge eins oder mehr eingeben.")
        sys.exit()
    text = args.text

    # choose search algorithm accoring to input arguments
    if args.ignore and args.naive:
        m = sm.StringMatching(string, text, case="ignore", method="naive")
    elif args.ignore:
        m = sm.StringMatching(string, text, case="ignore")
    elif args.naive:
        m = sm.StringMatching(string, text, method="naive")
    else:
        m = sm.StringMatching(string, text)
    position = m.matcher()
    if not position:
        print("Der Suchbegriff konnte nicht gefunden werden.")
    else:
        print(position)


if __name__ == "__main__":
    main()
