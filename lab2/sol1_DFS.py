from test import runtests
from collections import deque
_sentinel = object()

def toNeighbour(V, E):
    graph = [[] for _ in range(V)]
    for (x, y, c) in E:
        graph[x-1].append([y-1, c])
        graph[y-1].append([x-1, 0])
    return graph

def maxFlowDFS(V, E, s=0, t=_sentinel):
    if t is _sentinel:
        t = V - 1
    graph = toNeighbour(V, E)
    flow = 0

    def augumentingPath():
        nonlocal V, graph, s, t
        minimum = float('inf')

        que = deque()
        que.append((s, [s], [False] * V))

        while que:
            vertex, path, visited = que.pop()
            if vertex == t:
                return minimum, path+[t]
            visited[vertex] = True
            for neighbour, capacity in graph[vertex]:
                if not visited[neighbour] and capacity > 0:
                    minimum = min(minimum, capacity)
                    que.append((neighbour, path + [neighbour], visited))
        return 0, None

    delta, path = augumentingPath()
    while delta > 0:
        flow += delta
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            for j, (neighbour, _) in enumerate(graph[u]):
                if neighbour == v:
                    graph[u][j][1] -= delta
                    break
            for j, (neighbour, _) in enumerate(graph[v]):
                if neighbour == u:
                    graph[v][j][1] += delta
                    break
        delta, path = augumentingPath()
    return flow


if __name__ == "__main__":
    runtests(maxFlowDFS)
