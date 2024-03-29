# -*- coding: utf-8 -*-
# Elena Kröner
# Python 3.8

import os


class StringMatching:
    """
    Find position of a string in another string

    Parameters
    ----------
    string: str
        String that user searches for
    text: str
        Text, .txt-file or folder that string is searched in
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

    @staticmethod
    def __read_files(text, case=""):
        """
        Determine type of variable text and turn into searchable list of string

        Parameters
        ----------
        t : string, .txt-file or folder
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
        """
        Find position of search term in a larger string, using a naive search
        algorithm

        Returns
        -------
        string
            Contains all starting positions of search term in text
        """
        for t in self.text:
            found = []
            n = len(t)
            m = len(self.string)
            for s in range(n-m+1):
                if self.string == t[s:s+m]:
                    found.append(s)
            self.position.append(found)

        # if text contains multiple texts, return list as string per text,
        # otherwise return string
        if len(self.position) > 1:
            return ', '.join(map(str, self.position))
        else:
            return ', '.join(map(str, found))

    @staticmethod
    def __prefix(string):
        """
        Auxiliary function for KMP-matcher, compare string with itself

        Parameters
        ----------
        string: str
            String that is compared with itself

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
        Find position of search term in a larger string, using KMP-algorithm

        Returns
        -------
        string
            Contains all starting positions of search term in text
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

        # if text contains multiple texts, return list as string per text,
        # otherwise return string
        if len(self.position) > 1:
            return ', '.join(map(str, self.position))
        else:
            return ', '.join(map(str, found))


def main():
    naive_string = StringMatching("Braut", "Brautkleid bleibt Brautkleid und \
                                  Blaukraut bleibt Blaukraut.", method="naive")
    print("Beispiel für naiv und case-sensitive:\n"
        "Braut in Brautkleid bleibt Brautkleid und Blaukraut bleibt Blaukraut:",
          naive_string.matcher())

    naive_string_ignore = StringMatching("braut", "Brautkleid bleibt Brautkleid\
                                        und Blaukraut bleibt Blaukraut.",
                                        method="naive", case="ignore")
    print("Beispiel für naiv und case-insensitive:\n"
        "braut in Brautkleid bleibt Brautkleid und Blaukraut bleibt Blaukraut:",
          naive_string_ignore.matcher())

    kmp_string = StringMatching("bar",
                "RhabarberBarbaraBarbarenBartBarbierBierBarBärbel")
    print("Beispiel für KMP und case-sensitive:\n"
          "bar in RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
          kmp_string.matcher())

    kmp_string_ignore = StringMatching("bar",
                        "RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
                        case="ignore")
    print("Beispiel für KMP und case-insensitive:\n"
          "bar in RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
          kmp_string_ignore.matcher())

    kmp_file = StringMatching("tree", r"example\news.txt")
    print("Beispiel für default Suche in einer Datei:\n"
          "tree in example\\news.txt:", kmp_file.matcher())

    kmp_folder = StringMatching("Tree", r"example", method="naive",
                                case="ignore")
    print("Beispiel für case-insensitive Suche in einem Ordner:\n"
          "Tree im Ordner example:", kmp_folder.matcher())

    n_str = StringMatching("curious", "Curious and curiouser", method="naive")
    assert n_str.matcher() == "12"
    n_str_i = StringMatching("curious", "Curious and curiouser",
                             method="naive", case="ignore")
    assert n_str_i.matcher() == "0, 12"
    kmp_str = StringMatching("curious", "Curious and curiouser")
    assert kmp_str.matcher() == "12"
    kmp_str_i = StringMatching("curious", "Curious and curiouser",
                               case="ignore")
    assert kmp_str_i.matcher() == "0, 12"
    kmp_file = StringMatching("Heart", "example\\shortstory.txt")
    assert kmp_file.matcher() == "14"
    kmp_folder = StringMatching("Heart", "example\\")
    assert kmp_folder.matcher() == "[], [14]"


if __name__ == "__main__":
    main()
