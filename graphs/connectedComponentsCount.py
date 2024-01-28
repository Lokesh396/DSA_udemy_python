graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

print(graph.keys())

def explore(graph, node, visited):
    if node in visited:
        return False
    else: visited.add(node)
    for neighbor in graph[node]:
        explore(graph=graph, node=neighbor, visited=visited)
    return True

def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph.keys():
        if explore(graph, node, visited):
            count += 1
    
    return count

print(connected_components_count(graph=graph))