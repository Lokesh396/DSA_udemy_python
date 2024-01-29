graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def breadth_first_print(graph_data, source):
    queue = [source]
    while len(queue):
        current = queue.pop(0)
        print(current, end='\n')
        for neighbor in graph_data[current]:
            queue.append(neighbor)


breadth_first_print(graph_data=graph, source='a')
