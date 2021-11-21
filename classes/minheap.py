from . import path
import math

class MinHeap:
    def __init__(self, num_vertices: int):
        self.size: int = 0
        self.num_vertices: int = num_vertices
        self.path = []

    def heapsize(self):
        return self.size

    def parent(self, index: int) -> int:
        if index == 0: return 0
        return math.floor((index-1)/2)
    
    def left_child(self, index: int) -> int:
        return index*2+1
    
    def right_child(self, index: int) -> int:
        return index*2 + 2
    
    def swap_paths(self, a: path.Path, b: path.Path):
        temp = self.path[a]
        self.path[a] = self.path[b]
        self.path[b] = temp

    def minHeapify(self, index: int):
        left_child: int = self.left_child(index)
        right_child: int = self.right_child(index)

        # Check if the node has children
        isLeaf = False
        if index >= (self.size/2) and index <= self.size:
            isLeaf = True
        
        if not isLeaf and self.size > 0:
            print(self.path)
            print(left_child)
            print('index', index)
            if self.path[left_child].dist < self.path[index].dist:
                smallest = left_child
            else:
                smallest = index

            if self.path[right_child].dist < self.path[smallest].dist:
                smallest = right_child

            # if index is not the smallest then swap paths.
            if smallest != index:
                self.swap_paths(index, smallest)
                self.minHeapify(smallest)
    
    def insert(self, path: path.Path):
        self.path.append(path)
        self.size = self.size+1
        elem_index: int = self.size - 1
        parent_index: int = self.parent(elem_index)
        parent_dist: float = self.path[parent_index].dist
        elem_dist: float = self.path[elem_index].dist
        while elem_dist < parent_dist:
            self.swap_paths(elem_index, parent_index)
            elem_index = parent_index
        


    def extractMin(self) -> path.Path:
        root_elem: path.Path = self.path[0]
        self.path[0] = self.path.pop()
        
        self.size = self.size - 1
        self.minHeapify(0)
        return root_elem


h = MinHeap(1)
h.insert(Path('Test2', 2.0))
min: Path = h.extractMin()
print(min.dist)