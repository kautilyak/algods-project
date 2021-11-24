# Name: Kautilya Kondragunta

class Edge:
    def __init__(self, v, dist: float):
        self.destination = v
        self.dist = dist
        self.status = 'UP'