# -*- coding: utf-8 -*-
# Elena Kröner


class StringMatching:
    """
    Find position of a string in another string

    Attributes
    ----------
    string: str
        String that user searches for
    text: str
        String that 'string' is searched in
    method: str, default="kmp"
        Determine search method, either "kmp" or "naive"
    case: str, optional
        Turn off case-sensitivity if set to "ignore"
    """

    methods = ["kmp", "naive"]

    def __init__(self, string, text, method="kmp", case=""):
        if case == "ignore":
            self.string = list(string.lower())
            self.text = list(text.lower())
        else:
            self.string = list(string)
            self.text = list(text)
        if method in self.methods:
            self.method = method
        self.position = list()

    def matcher(self):
        if self.method == "naive":
            return self._naive()
        elif self.method == "kmp":
            return self._kmp_matcher()

    def _naive(self):
        n = len(self.text)
        m = len(self.string)
        for s in range(n-m):
            if self.string == self.text[s:s+m]:
                self.position.append(s)
        return ', '.join(map(str, self.position))

    def _prefix(self):
        """
        Compare string with itself

        Returns
        -------
        pi : dict
            Index of string as key with number of repeated characters from
            beginning as value.
        """
        m = len(self.string)
        pi = {0: 0}
        k = 0
        for q in range(1, m):
            while k > 0 and self.string[k] != self.string[q]:
                k = pi[k]
            if self.string[k] == self.string[q]:
                k += 1
            pi[q] = k
        return pi

    def _kmp_matcher(self):
        """
        Find position of search term in a larger string

        Returns
        -------
        list
            contains all starting positions of search term in larger string.
        """
        n = len(self.text)
        m = len(self.string)
        pi = self._prefix()
        q = 0
        for i in range(n):
            while q > 0 and self.string[q] != self.text[i]:
                q = pi[q]
            if self.string[q] == self.text[i]:
                q += 1
            if q == m-1:
                self.position.append(i-m+2)
                q = pi[q]
        return self.position


def main():
    # naive_string = StringMatching("Braut", "Brautkleid bleibt Brautkleid und \
    #                               Blaukraut bleibt Blaukraut.", method="naive")
    # print(naive_string.matcher())
    # naive_case_ignore = StringMatching("braut", "Brautkleid bleibt Brautkleid\
    #                                    und Blaukraut bleibt Blaukraut.",
    #                                    method="naive", case="ignore")
    # print(naive_case_ignore.matcher())

    kmp_string = StringMatching("bar", "RhabarberBarbaraBarbarenBartBarbierBierBarBärbel")
    print(kmp_string.matcher())
    kmp_string = StringMatching("bar", "RhabarberBarbaraBarbarenBartBarbierBierBarBärbel",
                                case="ignore")
    print(kmp_string.matcher())


if __name__ == "__main__":
    main()
