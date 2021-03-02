# -*- coding: utf-8 -*-
# Elena Kröner
# Python 3.8

import argparse
import os
import sys

import searchalgorithm as sm


def readfiles(t):
    """
    Determine type of variable 'text' and turn into searchable list of string

    Parameters
    ----------
    t : string, .txt-file or foulder
        Text that will be transformed based on its type.

    Returns
    -------
    texts : list of string or list of lists
        List with text that will be searched in, either a string or multiple
            sublists if input is a foulder with multiple .txt-files.

    """
    texts = []
    if os.path.isfile(t):
        with open(t, "r", encoding="utf-8") as t:
            text = t.read()
            texts.append(text)
    elif os.path.isdir(t):
        for root, dirs, files in os.walk(sys.argv[-1]):
            for filename in files:
                with open(root+"\\"+filename, "r", encoding="utf-8") as t:
                    text = t.read()
                    texts.append(text)
    else:
        text = sys.argv[-1]
        texts.append(text)
    return texts


def define_argparser():
    parser = argparse.ArgumentParser(description="String Matcher")
    parser.add_argument("suche", help="Suche einen String in einem Text")
    parser.add_argument("-i", "--ignore", action="store_true",
                        help="Groß- und Kleinschreibung ignorieren")
    parser.add_argument("-n", "--naive", action="store_true",
                        help="Den naiven Suchalgorithmus verwenden")
    parser.add_argument("suchbegriff", type=str,
                        help="Das Wort, nach dem gesucht werden soll")
    parser.add_argument("text", type=str, help="String, .txt-Dokument oder \
                        Ordner, in dem gesucht werden soll")
    args = parser.parse_args()
    return args


def main():
    args = define_argparser()

    # check if string is not empty and transform it with readfiles-function
    string = sys.argv[-2]
    if not string:
        print("Bitte einen Suchbegriff der Länge eins oder mehr eingeben.")
        sys.exit()
    t = sys.argv[-1]
    texts = readfiles(t)

    for text in texts:
        # choose search algorithm accoring to input arguments
        if args.ignore and args.naive:
            m = sm.StringMatching(string, text, case="ignore", method="naive")
            print("Ignoriere Groß- und Kleinschreibung, suche mit naivem Algorithmus")
        elif args.ignore:
            m = sm.StringMatching(string, text, case="ignore")
            print("Ignoriere Groß- und Kleinschreibung")
        elif args.naive:
            print("Verwende naiven Algorithmus")
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
