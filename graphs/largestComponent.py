# graph = {
#     0: [8, 1, 5],
#     1: [0],
#     5: [0, 8],
#     8: [0, 5],
#     2: [3, 4],
#     3: [2, 4],
#     4: [3, 2]
# }

graph = {
    3: [],
    4:[6],
    6:[4,5,7,8],
    8:[6],
    7:[6],
    5:[6],
    1:[2],
    2:[1]
}


def component_count(graph, node, visited):
    if node in visited:
        return 0
    else: visited.add(node)
    stack = [node]
    count = 0
    while(len(stack)):
        current = stack.pop()
        count += 1
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
    return count


def largest_component(graph):
    largest = 0
    visited = set()
    for node in graph.keys():
        count = component_count(graph=graph, node=node, visited=visited)
        largest = max(largest, count)
    return largest

print(largest_component(graph=graph))