graph ={
    'a': ['b', 'c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

def breadthFirstPrint(graph, source):
    queue = [source]
    while(len(queue)):
        current = queue.pop(0)
        print(current, end='\n')
        for neighbor in graph[current]:
            queue.append(neighbor)



breadthFirstPrint(graph=graph, source='a')