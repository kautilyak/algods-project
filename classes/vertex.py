from . import linkedlist
import numpy as np

class Vertex:
    def __init__(self, name):
        self.name = name
        self.status = 'UP'
        self.dist = np.inf
        self.pred = None
        self.adjacent = linkedlist.LinkedList()
        self.color: str = None
        self.finish: int = None
        self.reachable = []
    
    def reset(self):
        self.dist = np.inf
        self.pred = None