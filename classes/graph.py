from typing import OrderedDict
from . import path
from . import error
from . import edge
from . import vertex
from . import linkedlist
import heapq
import numpy as np
import collections

class Graph:
    def __init__(self):
        self.vertexMap =  dict()

    # Initializes the vertex output info prior to running
    # any shortest path algorithm.
    def clearAll(self):
        for v in self.vertexMap.values():
            v.reset()

    # If vertexName is not present, add it to vertexMap.
    # In either case, return the Vertex.
    def  getVertex(self, vertexName: str):
        if vertexName not in self.vertexMap:
            v = vertex.Vertex(vertexName)
            self.vertexMap[vertexName] = v
        v = self.vertexMap[vertexName]
        return  v

    # Add a new edge to the graph.
    # Modify this to handle weight inputs aswell
    def addEdge(self, sourceName: str,  destName: str, weight: float):
        v: vertex.Vertex = self.getVertex(sourceName)
        w: vertex.Vertex = self.getVertex(destName)
        isEdge = False
        current: linkedlist.Node or None = v.adjacent.head
        # if the vertex v has edges.
        
        while(current != None):
            # loop through the adj linked list until next is not None. (tail)
            if w.name == current.val.destination.name:
                # it is present in the adj list
                isEdge = True
                # Change transmission time
                current.val.dist = weight
                
            
            # iterate
            current = current.next

        if not isEdge:
            # if not an edge, then flag is falsy.
            # create new edge to the list
            new_edge: edge.Edge = edge.Edge(w, weight)
            
            # add this new edge to the adj list of the source vertex 'v'
            v.adjacent.insert(new_edge)
    

    # remove an existing edge from the graph.
    # Do not delete the vertices.
    # If edge does not exist do nothing.
    # Note: This may cause two vertices to be connected by a directed edge in one direction, but not the other.
    def deleteEdge(self, sourceName: str, destName: str):
        v: vertex.Vertex = self.getVertex(sourceName)
        w: vertex.Vertex = self.getVertex(destName)

        # Get the adjacency list of Edges of the source vertex
        current = v.adjacent.head
        while current != None:
            if current.val.destination.name == destName:
                # edge exists, remove the edge.
                v.adjacent.deleteNode(current.val)
                return
            # iterate    
            current = current.next

    # Mark the directed edge as “down” and therefore unavailable for use.
    # The response to an edgedown (or edgeup) query should mark only the specified directed edge as “down” (or “up”).
    def edgeDown(self, sourceName: str, destName: str):
        v: vertex.Vertex = self.getVertex(sourceName)
        w: vertex.Vertex = self.getVertex(destName)

        # head of the adjacent edges to loop
        current = v.adjacent.head

        while current != None:
            # if edge exists in the list
            if current.val.destination.name == destName:
                # set edge status to `DOWN`
                current.val.status = 'DOWN'
                return
            current = current.next

    # Mark the directed edge as "up" and therefore unavailable for use.
    # The response to an edgedown (or edgeup) query should mark only the specified directed edge as up (or “down”).
    def edgeUp(self, sourceName: str, destName: str):
        v: vertex.Vertex = self.getVertex(sourceName)
        w: vertex.Vertex = self.getVertex(destName)

        # head of the adjacent edges to loop
        current = v.adjacent.head

        while current != None:
            # if edge exists in the list
            if current.val.destination.name == destName:
                # set edge status to `UP`
                current.val.status = 'UP'
                return
            current = current.next

    # Mark the vertex as “down”. None of its edges can be used.
    # Marking a vertex as “down” should not cause any of its incoming or outgoing edges to be marked as “down”.
    # the graph can have “up” edges going to and leaving from a “down” vertex. However a path through such a “down” vertex cannot be used as a valid path.
    # input must be a vertex name. Not the vertex object itself.
    def vertexDown(self, _vertex: str):
        if _vertex in self.vertexMap:
            v: vertex.Vertex = self.vertexMap[_vertex]
            v.status = 'DOWN'
        else:
            print('Vertex not found.')
    
    # symmetrical to vertexDown() but 'UP'
    def vertexUp(self, _vertex: str):
        if _vertex in self.vertexMap:
            v: vertex.Vertex = self.vertexMap[_vertex]
            v.status = 'UP'
        else:
            print('Vertex not found.')

    

    # Djikstra's algorithm implementation for shortest path.
    def Djikstra(self, sourceVertex: str):
        self.clearAll()
        queue = []

        # check if vertex is available.
        if sourceVertex not in self.vertexMap:
            print('Vertex not found.')
            return
        init_v: vertex.Vertex = self.vertexMap[sourceVertex]
        # check if vertex is UP.
        if init_v.status == 'DOWN': 
            print('Vertex is down - cannot use as source.')
            return

        # Set initial vertex distance to 0
        init_v.dist = 0.0
        heapq.heappush(queue, path.Path(init_v.name, init_v.dist))

        # while queue is not empty, BFS.
        while len(queue) != 0:
            min: path.Path = heapq.heappop(queue)
            v: vertex.Vertex = self.getVertex(str(min.name))
            
            # for every edge of v. Add to queue.
            current: linkedlist.Node = v.adjacent.head
            while current != None:
                # w -> Edge
                e: edge.Edge = current.val
                w: vertex.Vertex = e.destination
                weight: float = e.dist

                # Check if Edge is up and destination Vertex is up
                if e.status == 'UP' and w.status == "UP":

                    if weight < 0:
                        raise error.GraphError('Weight can\'t be negative')

                    # if the destination vertex's distance is greater than the source vertex dist + weight
                    # then, reset the predecessor and weight of the dest vertex.
                    if w.dist > v.dist + weight:
                        w.dist = v.dist + weight
                        w.pred = v

                        # insert new discovered vertex onto the queue.
                        edited = False
                        for obj in queue:
                            if w.name == obj.name:
                                obj.dist = w.dist
                                edited = True
                        if not edited:
                            heapq.heappush(queue, path.Path(w.name, w.dist))

                current = current.next


    # Driver routine to print total distance.
    # It calls recursive routine to print shortest path to
    # destNode after a shortest path algorithm has run.
    def printPath(self, destName: str):
        w: vertex.Vertex = self.vertexMap[destName]
        if w is None:
            print("Destination vertex not found")
        elif np.isinf(w.dist):
            raise Exception(destName + " is unreachable")
        else:
            print("(Distance is: " + str(w.dist) + ") ", end ="")
            self.printPath_(w)
        print()

    # Recursive routine to print shortest path to dest
    # after running shortest path algorithm. The path
    # is known to exist.
    def printPath_(self, dest: vertex.Vertex):
        if dest.pred is not None:
            self.printPath_(dest.pred)
            print(" to ", end ="")
        print(dest.name, end ="")

    # print the graph
    def printGraph(self):
        for key, value in sorted(self.vertexMap.items(), key=lambda x: x[0]):
            print(key)
            current: linkedlist.Node = value.adjacent.head
            while current != None:
                print('\t', current.val.destination.name, current.val.dist)
                current = current.next
                
    # The printReachable() function goes over the vertexMap once for every vertex (V). 
    # Within the vertex iteration, it goes through the adjacency list of each vertex - which is a list of edges (E) each vertext is connected by.
    # So we can say that the total time complexity for the function is O(V+E).
    def printReachable(self):
        for key, value in sorted(self.vertexMap.items(), key=lambda x: x[0]):
            currentVertex: vertex.Vertex = value
            if currentVertex.status == 'UP':
                print(key)
                current: linkedlist.Node = currentVertex.adjacent.head
                while current != None:
                    currentEdge: edge.Edge = current.val
                    if currentEdge.status == 'UP':
                        print('\t', currentEdge.destination.name)
                    current = current.next
        
