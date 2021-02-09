# -*- coding: utf-8 -*-
# Elena Kröner


class StringMatching:
    """Find position of a string in another sting, text or multiple texts"""

    def __init__(self, string, text, method="kmp"):
        self.string = string
        self.text = text
        self.position = list()

    def naive(self):
        n = len(self.text)
        m = len(self.string)
        for s in range(n):
            if list(self.string) == list(self.text)[s:s+m]:
                self.position.append(s)
        return ', '.join(map(str, self.position))

    def _prefix(self):
        pass

    def kmp_matcher(self):
        pass


def main():
    match = StringMatching("kleid", "Brautkleid bleibt Brautkleid und Blaukraut bleibt Blaukraut.")
    print(match.naive())


if __name__ == "__main__":
    main()
