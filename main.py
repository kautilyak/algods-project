from classes.graph import Graph


g = Graph()
g.addEdge('House', 'College', 10.0)
g.addEdge('House', 'Garage', 2.0)
g.addEdge('House', 'Aunt', 22.0)
g.addEdge('Garage', 'College', 7.0)
g.addEdge('College', 'Aunt', 2.0)
g.addEdge('Aunt', 'House', 12.0)
#print('Vertex Map', g.vertexMap)
for vertex, val in g.vertexMap.items():
    # Test edge additions
    print(vertex, val.adjacent.length, "edges")

    # # TEST EDGE DOWN
    # current = val.adjacent.head
    # while current != None:
    #     if current.val.status == 'DOWN':
    #         print(current.val.destination.name, 'is down')
    #     current = current.next


g.Djikstra('House')
