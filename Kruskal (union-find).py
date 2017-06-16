parent = dict()
rank = dict()
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    print (edges)
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

graph = {'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],'edges': {(3, 'A', 'B'), (4, 'A', 'E'), (7, 'A', 'F'), (5, 'B', 'C'), (8, 'B', 'F'), (4, 'C', 'D'),(6,'C','F'),(8,'D','D'),(2,'D','E'),(5,'E','F')}}
print(kruskal(graph))
