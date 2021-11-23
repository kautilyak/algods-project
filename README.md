# algods-project
 Final project for Algorithms and Data Structures class of Fall 2021. [ITCS-6114/8114]
 
 **NAME** : _Kautilya Kondragunta_ <br>
 **ID**: _801231832_

# Project Introduction
Consider a data communication network that must route data packets (email, MP3 files, or video
files, for example). Such a network consists of routers connected by physical cables or links. A
router can act as a source, a destination, or a forwarder of data packets. We can model a network
as a graph with each router corresponding to a vertex and the link or physical connection between
two routers corresponding to a pair of directed edges between the vertices.
A network that follows the OSPF (Open Shortest Path First) protocol routes packets using
Dijkstra’s shortest path algorithm. The criteria used to compute the weight corresponding to a
link can include the time taken for data transmission, reliability of the link, transmission cost, and
available bandwidth. Typically each router has a complete representation of the network graph
and associated information available to it.
For the purposes of this project, each link has associated with it the transmission time taken
for data to get from the vertex at one end to the vertex at the other end. You will compute the
best path using the criterion of minimizing the total time taken for data to reach the destination.
The shortest time path minimizes the sum of the transmission times of the links along the path.
The network topology can change dynamically based on the state of the links and the routers.
For example, a link may go down when the corresponding cable is cut, and a vertex may go down
when the corresponding router crashes. In addition to these transient changes, changes to a network
occur when a link is added or removed.

# Taks
1. Building the initial graph
2. Updating the graph to reflect changes.
3. Finding the shortest path between any two vertices in the graph based on its current state.
4. Printing the graph, and finding reachable sets of vertices.



# Usage
1. Clone the repository 
2. Run using command `python -m graph INPUT.TXT` (INPUT file network.txt is already provided)
3. Use any of the following commands to manipulate the graph.

# Commands:
- `path` _SOURCE_ _DESTINATION_ 
- `addedge` _SOURCE_ _DESTINATION_ _WEIGHT_
- `deleteedge` _SOURCE_ _DESTINATION_  
- `edgedown` _SOURCE_ _DESTINATION_
- `edgeup` _SOURCE_ _DESTINATION_  
- `vertexdown` _VERTEX_NAME_ 
- `vertexup` _VERTEX_NAME_ 
- `print` 
- `reachable`
- `quit`


# Classes used
 - LinkedList
 - Vertex
 - Edge
 - Path  
 - Graph



## LinkedList
 - Represents the adjacency list of all the edges for a vertex in the graph.
 - Should contain a `Node` and a `List` class.
 > **Node** class  stores a `value` and a `next` variable to point to the next node.
 > **List** class initializes and stores the `head`, `tail` and `length` properties.
 >> Additionally it has methods to `push` to the head, `insert`, `pop`, `get` methods.

## Vertex
- Represents each node in the graph.
> Should contain meta data on `name` (String), `pred` (Vertex), `dist` (number), Adjacent vertices `adj` (Linkedlist), `link_status` (String)
 
## Edge
- Represents the connection between two vertices.
> Contains meta data on `dist` (weight), `destination`(vertex) `status` 

## Path
- Represents the queue item for the min-binary heap structure.
> Contains meta data on the `name` (Vertex name) and `dist` (distance)

## Graph
This is where most of the functionality lies. It has all the methods related to manipulating the graph.
### Main methods:
- `getVertex()` - Get the vertex object
- `addEdge()` - Add edge to the graph between two vertices
- `deleteEdge()`-  Delete edge in the graph between two vertices
- `edgeDown()`- Mark edge as DOWN between vertices
- `edgeUp()`- Mark edge as UP between vertices
- `vertexDown()` - Mark vertex as DOWN between vertices
- `vertexUp()`- Mark vertex as UP between vertices
- `Djikstra()` - Find the shortest path in the graph from the source vertex
- `printPath()` - Print the shortest path in the graph from source to destination
- `printReachable()` - Print all the reachable vertices and edges in the graph.
- `printGraph()` - Print all the vertices and edges in the graph.


## Time complexity of printReachable():

- The `printReachable()` function goes over the *vertexMap* once for every vertex  (V). Within the vertex iteration, it goes through the adjacency list of each vertex - which is a list of edges (E) each vertext is connected by. So we can say that the total time complexity for the function is **O(V+E)**.



