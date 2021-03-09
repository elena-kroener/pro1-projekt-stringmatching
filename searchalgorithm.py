# -*- coding: utf-8 -*-
# Elena Kröner
# Python 3.8

import os


class StringMatching:
    """
    Find position of a string in another string

    Attributes
    ----------
    string: str
        String that user searches for
    text: str
        Text that string is searched in
    method: str, default="kmp"
        Determine search method, either "kmp" or "naive"
    case: str, optional
        Turn off case-sensitivity if set to "ignore"
    """

    methods = ["kmp", "naive"]

    def __init__(self, string, text, method="kmp", case=""):
        if case == "ignore":
            self.string = string.lower()
            self.text = self.__read_files(text, case="ignore")
        else:
            self.string = string
            self.text = self.__read_files(text)
        if method in self.methods:
            self.method = method
        self.position = list()

    def matcher(self):
        if self.method == "naive":
            return self.__naive()
        elif self.method == "kmp":
            return self.__kmp_matcher()

    def __read_files(self, text, case=""):
        """
        Determine type of variable text and turn into searchable list of string

        Parameters
        ----------
        t : string, .txt-file or foulder
            Text that will be transformed based on its type.
        case : string, default=""
            set to case-insensitive if case="ignore"

        Returns
        -------
        texts : list of string or list of lists
            List with text that will be searched in, either a string or
            multiple sublists if input is a foulder with multiple .txt-files.
        """
        texts = []
        if os.path.isfile(text):
            with open(text, "r", encoding="utf-8") as t:
                text = t.read()
                texts.append(text)
        elif os.path.isdir(text):
            for root, dirs, files in os.walk(text):
                for filename in files:
                    with open(root+"\\"+filename, "r", encoding="utf-8") as t:
                        text = t.read()
                        texts.append(text)
        else:
            texts = [text]
        if case == "ignore":
            texts = [text.lower() for text in texts]
        return texts

    def __naive(self):
        for t in self.text:
            found = []
            n = len(t)
            m = len(self.string)
            for s in range(n-m+1):
                if self.string == t[s:s+m]:
                    found.append(s)
            self.position.append(found)
        if len(self.position) > 1:
            return ', '.join(map(str, self.position))
        else:
            return ', '.join(map(str, found))

    @staticmethod
    def __prefix(string):
        """
        Compare string with itself

        Returns
        -------
        pi : dict
            Index of string as key with number of repeated characters from
            beginning as value.
        """
        m = len(string)
        pi = {0: 0}
        k = 0
        for q in range(1, m):
            while k > 0 and string[k] != string[q]:
                k = pi[k]
            if string[k] == string[q]:
                k += 1
            pi[q] = k
        return pi

    def __kmp_matcher(self):
        """
        Find position of search term in a larger string

        Returns
        -------
        list
            Contains all starting positions of search term in larger string.
        """
        for t in self.text:
            found = []
            n = len(t)
            m = len(self.string)
            pi = self.__prefix(self.string)
            q = 0
            for i in range(n):
                while q > 0 and self.string[q] != t[i]:
                    q = pi[q]
                if self.string[q] == t[i]:
                    q += 1
                if q == m:
                    found.append(i-m+1)
                    q = pi[q-1]
            self.position.append(found)
        if len(self.position) > 1:
            return ', '.join(map(str, self.position))
        else:
            return ', '.join(map(str, found))


def main():
    naive_string = StringMatching("Braut", "Brautkleid bleibt Brautkleid und \
                                  Blaukraut bleibt Blaukraut.", method="naive")
    print("Beispiel für naiv und case-sentitve:\n"
        "Braut in Brautkleid bleibt Brautkleid und Blaukraut bleibt Blaukraut:",
          naive_string.matcher())

    naive_string_ignore = StringMatching("braut", "Brautkleid bleibt Brautkleid\
                                        und Blaukraut bleibt Blaukraut.",
                                        method="naive", case="ignore")
    print("Beispiel für naiv und case-insentitve:\n"
        "braut in Brautkleid bleibt Brautkleid und Blaukraut bleibt Blaukraut:",
          naive_string_ignore.matcher())

    kmp_string = StringMatching("bar",
                "RhabarberBarbaraBarbarenBartBarbierBierBarBärbel")
    print("Beispiel für KMP und case-sentitve:\n"
          "bar in RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
          kmp_string.matcher())

    kmp_string_ignore = StringMatching("bar",
                        "RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
                        case="ignore")
    print("Beispiel für KMP und case-insentitve:\n"
          "bar in RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
          kmp_string_ignore.matcher())

    kmp_file = StringMatching("tree", r"example\news.txt")
    print("Beispiel für default Suche in einer Datei:\n"
          "tree in news.txt:", kmp_file.matcher())

    kmp_folder = StringMatching("Tree", r"example", case="ignore")
    print("Beispiel für case-insensitive Suche in einem Ordner:\n"
          "Tree im Ordner example:", kmp_folder.matcher())


if __name__ == "__main__":
    main()
