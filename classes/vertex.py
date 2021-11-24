# Name: Kautilya Kondragunta

from . import linkedlist
import numpy as np

class Vertex:
    def __init__(self, name):
        self.name = name
        self.status = 'UP'
        self.dist = np.inf
        self.pred = None
        self.adjacent = linkedlist.LinkedList()
    
    def reset(self):
        self.dist = np.inf
        self.pred = None

    def __lt__(self, other):
        return self.name < other.name