def bfs(graph, start):
  path=[]
  q=[start]
  while q:
    v=q.pop(0)  #THIS WILL DELETE FROM FRONT FROM 0th position hence will act as a queue
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print(' bfs ', bfs(graph, 'A'))