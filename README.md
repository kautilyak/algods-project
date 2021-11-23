# algods-project
 Final project for Algorithms and Data Structures class of Fall 2021. [ITCS-6114/8114]
 
 **NAME** : _Kautilya Kondragunta_ <br>
 **ID**: _801231832_

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


# Classes Required
 - LinkedList
 - Vertex
 - Edge
 - Path  
 - Graph



## LinkedList
 Should contain a `Node` and a `List` class.
 > **Node** class  stores a `value` and a `next` variable to point to the next node.
 > **List** class initializes and stores the `head`, `tail` and `length` properties.
 >> Additionally it has methods to `push` to the head, `insert`, `pop`, `get` methods.

## Vertex
 Should contain meta data on `name` (String), `pred` (Vertex), `dist` (number), Adjacent vertices `adj` (Linkedlist), `link_status` (String)
 
## Edge
Contains meta data on `dist` (weight), `destination`(vertex) `status` 

## Path
Contains meta data on the `name` (Vertex name) and `dist` (distance)

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



