# -*- coding: utf-8 -*-
# Elena Kröner

import argparse
import os
import sys

import stringmatching as sm


def readfiles(t):
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


def main():
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


    # if len(sys.argv) < 3 or sys.argv[1] != "suche":
    #     parser.print_help()
    #     sys.exit()

    args = parser.parse_args()
    print(args)    

    string = sys.argv[-2]
    t = sys.argv[-1]
    texts = readfiles(t)

    for text in texts:
        print(text)
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
        print(position)

        # match = matching(string, text, case="i")
        # print(match)
        


if __name__ == "__main__":
    main()
