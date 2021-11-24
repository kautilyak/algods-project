# Name: Kautilya Kondragunta

from numpy import degrees
from classes.error import GraphError
from classes.graph import Graph
import sys

# Process a request; return false if end of file.
def processRequest(g: Graph):
    try:
        print("Enter command: ", end ="")
        command = input()
        command = command.strip().split(" ")
        query: str = command[0]
        
        if query.lower() == 'path':
            startName: str = command[1] # Source
            destName: str = command[2]  # Destination
            g.Djikstra(startName) # Find Shortest path
            g.printPath(destName) # Print path

        if query.lower() == 'addedge':
            startName: str = command[1] # Source
            destName: str = command[2]  # Destination
            weight: float = float(command[3])  # Destination
            g.addEdge(startName, destName, weight)
            
        if query.lower() == 'deletedge':
            startName: str = command[1] # Source
            destName: str = command[2]  # Destination
            g.deleteEdge(startName, destName)

        if query.lower() == 'edgedown':
            startName: str = command[1] # Source
            destName: str = command[2]  # Destination
            g.edgeDown(startName, destName)

        if query.lower() == 'edgeup':
            startName: str = command[1] # Source
            destName: str = command[2]  # Destination
            g.edgeUp(startName, destName)
        
        if query.lower() == 'vertexdown':
            vertexName: str = command[1] # Vertex Name
            g.vertexDown(vertexName)

        if query.lower() == 'vertexup':
            vertexName: str = command[1] # Vertex Name
            g.vertexUp(vertexName)
            
        if query.lower() == 'print':
            g.printGraph()
        
        if query.lower() == 'reachable':
            g.printReachable()
        
        if query.lower() == 'quit':
            return False

    except Exception as e:
        print(e)
    return  True

# A main routine that:
# 1. Reads a file containing edges (supplied as a command-line parameter);
# 2. Forms the graph;
# 3. Repeatedly prompts for two vertices and
#    runs the shortest path algorithm.
# The data file is a sequence of lines of the format
#    source destination
def main():
    g = Graph()
    fin = sys.argv[1]
    with open(fin) as f:
        lines = f.readlines()
    #  Read the edges and insert
    for line in lines:
        line = line.strip().split(" ")
        if (len(line) != 3):
            print("Skipping ill-formatted line " + line)
            continue
        source: str = line[0]
        dest: str = line[1]
        weight: float = float(line[2])
        g.addEdge(source, dest, weight)
    print("File read...")
    print(str(len(g.vertexMap)) + " vertices")
    try:
        while processRequest(g):
            pass
    except KeyboardInterrupt:
        print('\n\nQuitting program...')

if __name__=="__main__":
    main()
