
# directed acyclic graph
adj_list = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4, 5],
    4: [],
    5: []
}

def dfs(ind, nodes, visit, graph):
    visit[ind] = True

    for edge in graph[ind]:
        if visit[edge] == False:
            dfs(edge, nodes=nodes, visit=visit, graph=graph)
    nodes.append(ind)


def topologicalsort(graph):
    n = len(graph)
    visted = [False] * n
    ordering = [-1] * n
    order = n -1 
    
    for i in range(n):
        if not visted[i]:
            visitedNodes = []
            dfs(i,visitedNodes, visted, graph)
            for node in visitedNodes:
                ordering[order] = node
                order -= 1
    
    return ordering


print(topologicalsort(adj_list))