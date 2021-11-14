from linkedlist import LinkedList

class Vertex:
    def __init__(self, name):
        self.name = name
        self.status = 'UP'
        self.dist = float('inf')
        self.pred = None
        self.adjacent = LinkedList()