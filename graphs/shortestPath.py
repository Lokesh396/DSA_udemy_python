edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
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

def shortest_path(edges, nodeA, nodeB):
    graph = buildGraph(edges=edges)
    visited = set()
    visited.add(nodeA)
    queue = [[nodeA, 0]]
    while(len(queue)):
        current = queue.pop(0)
        currentNode, edgeCount = current[0], current[1]
        if currentNode == nodeB:
            return edgeCount
        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                queue.append([neighbor, edgeCount + 1])
                visited.add(neighbor)
    
    return -1



print(shortest_path(edges=edges, nodeA='w', nodeB='z'))