class StringPair:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def key(self):
        return self.s1

    def value(self):
        return self.s2
