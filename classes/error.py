# Name: Kautilya Kondragunta

class GraphError(Exception):
    """Exception raised for errors in the graph.

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, msg: str):
        self.message = msg