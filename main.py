from classes.error import GraphError
from classes.graph import Graph
import sys

# Process a request; return false if end of file.
def processRequest(g: Graph):
    try:
        print("Enter start node: ", end ="")
        startName = input()
        print("Enter destination node: ", end ="")
        destName = input()
        g.Djikstra(startName)
        g.printPath(destName)
    except Exception as e:
        print(e)
        return  False
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
    while processRequest(g):
        pass

if __name__=="__main__":
    main()
