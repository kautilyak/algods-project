from path import Path
import math

class MinHeap:
    def __init__(self, size, num_vertices):
        self.size = size
        self.num_vertices = num_vertices
        self.path = [Path] * num_vertices + 1 
        self.path[0] = Path('null', float(0))

    def heapsize(self):
        return self.size

    def parent(self, index):
        return math.floor(index/2)
    
    def left_child(self, index):
        return index*2
    
    def right_child(self, index):
        return index*2 + 1
    
    def swap_paths(self, a, b):
        self.path[a], self.path[b] = self.path[b], self.path[a]

    def minHeapify(self, index):
        left_child = self.left_child(index)
        right_child = self.right_child(index)

        # Check if the node has children
        isLeaf = False
        if index-1 >= (self.size/2) and index <= self.size:
            isLeaf = True
        
        if not isLeaf and self.size > 0:
            if self.path[left_child] < self.path[index]:
                smallest = left_child
            else:
                smallest = index
            
            if self.path[right_child] < self.path[smallest]:
                smallest = right_child

            # if index is not the smallest then swap paths.
            if smallest != index:
                self.swap_paths(index, smallest)
                self.minHeapify(smallest)