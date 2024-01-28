graph ={
    'a': ['b', 'c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

# def depthFirstPrint(graph, source):
#     stack = [source]
#     while(len(stack)):
#         cur = stack.pop()
#         print(cur, end=' ')
#         for neighbor in (graph[cur]):
#             stack.append(neighbor)

def depthFirstPrint(graph, source):
    print(source,end='\n')
    for i in (graph[source]):
        depthFirstPrint(graph=graph, source=i)


depthFirstPrint(graph=graph, source='a')