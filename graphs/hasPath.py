graph = {
    'f':['g', 'i'],
    'g':['h'],
    'h':[],
    'i':['g', 'k'],
    'j':['i'],
    'k':[]
}

def has_path_depth(graph, source, dest):
    if source == dest:
        return True
    for neighbor in graph[source]:
        if has_path_depth(graph=graph, source=neighbor, dest=dest):
            return True
    
    return False

print(has_path_depth(graph=graph, source='f', dest='j'))


def has_path_breath(graph, source, dest):
    queue = [source]
    while(len(queue)):
        current = queue.pop(0)
        if current == dest:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


print(has_path_breath(graph=graph, source= 'f', dest='j'))