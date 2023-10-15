from test import runtests
from queue import Queue
_sentinel = object()


def toNeighbour(V, E):
    graph = [[] for _ in range(V)]
    for (x, y, c) in E:
        graph[x-1].append([y-1, c])
        graph[y-1].append([x-1, 0])
    return graph


def maxFlowBFS(V, E, s=0, t=_sentinel):
    if t is _sentinel:
        t = V - 1
    graph = toNeighbour(V, E)
    flow = 0

    def augumentingPath():
        nonlocal V, graph, s, t
        size = [float('inf')] + [0] * (V-1)
        parent = [None] * V

        que = Queue()
        que.put(s)

        while not que.empty():
            vertex = que.get()
            if vertex == t:
                path = []
                while vertex != s:
                    path.append(vertex)
                    vertex = parent[vertex]
                path.append(s)
                path.reverse()
                return size[t], path
            for neighbour, capacity in graph[vertex]:
                minimum = min(size[vertex], capacity)
                if capacity > 0 and size[neighbour] < minimum:
                    size[neighbour] = minimum
                    parent[neighbour] = vertex
                    que.put(neighbour)
        return 0, None

    delta, path = augumentingPath()
    while delta > 0:
        flow += delta
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
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
    runtests(maxFlowBFS)
