from heapq import *
def prim(nodes, edges):
    graph = {i: [] for i in nodes}
    print(graph)
    for cost,u, v  in edges:
        graph[u].append([cost, u, v])
        graph[v].append([cost, v, u])
    MST = []
    used = [nodes[0]]
    usable_edges = graph[nodes[0]]
    heapify(usable_edges)
    while usable_edges:
        [cost,u, v] = heappop(usable_edges)
        if v not in used:
            used += [v]
            MST.append([cost,u, v])
            for e in graph[v]:
                if e[2] not in used:
                    heappush(usable_edges, e)
    return MST
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [(3, 'A', 'B'), (4, 'A', 'E'), (7, 'A', 'F'), (5, 'B', 'C'), (8, 'B', 'F'), (4, 'C', 'D'),(6,'C','F'),(8,'D','D'),(2,'D','E'),(5,'E','F')]
print(prim(nodes, edges))