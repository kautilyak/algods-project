class Path:
    def __init__(self, name: str ,dist: float):
        self.name = name
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist