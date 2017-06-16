def initialize(graph, source):      # Step 1: For each node prepare the destination and predecessor
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p
def relax(node, neighbour, graph, d, p):        # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]            # Record this lower distance
        p[neighbour] = node
def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it
    for u in graph:         # Step 3: check for negative-weight cycles
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
    return d, p
graph = {
        'a': {'b': -4, 't':  -3},
        'b': {'d':  -1, 'e':  -2},
        'c': {'b': 8,'t':3},
        'd': {'a':  6, 't':  4},
        'e': {'c': -3, 't':2},
        't':{}
        }
d, p = bellman_ford(graph, 'a')
print(d,p)
