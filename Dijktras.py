import heapq as hq
def Djik(graph,start):
    n = len(graph)
    Q = [[0, start]]
    print("source")
    print(Q)
    d = [999 for i in range(n)]
    d[start]=0
    while Q:
        [length, u] = hq.heappop(Q)
        for v in range(n):
            if d[v] > d[u] + graph[u][v]:
                d[v] = d[u] + graph[u][v]
                hq.heappush(Q, [d[v], v])
    return d
graph = [[0,  10,  999,  999, 100], [10,  0 ,50,  999,999],[999,  50,  0,  20,10], [999,  999,  20,0,60],[100,999,10,60,0]]
d = Djik(graph,0)
print("min shortest path to nodes")
print(d)