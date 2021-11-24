# Name: Kautilya Kondragunta


class Path:
    def __init__(self, name: str ,dist: float):
        self.name = name
        self.dist = dist

    # Makes the object comparable.
    def __lt__(self, other):
        return self.dist < other.dist
