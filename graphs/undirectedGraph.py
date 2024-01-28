edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def buildGraph(edges):
    graph = {}
    for edge in edges:
        a,b = edge[0], edge[1]
        if a not in graph:
            graph[a] =[]
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

def hasPath(graph, source, dest, visited):
    if source in visited:
        return False
    else:
        visited.add(source)
    if source == dest:
        return True
    for neighbor in graph[source]:
        if hasPath(graph=graph, source=neighbor, dest=dest, visited=visited):
            return True
    return False

def undirectedGraphpath(edges, nodeA, nodeB):
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())





print(undirectedGraphpath(edges=edges, nodeA='i', nodeB='k'))
