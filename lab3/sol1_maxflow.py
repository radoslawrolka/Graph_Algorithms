from test import runtests
from queue import Queue
_sentinel = object()

# O(V * E^2*V)

def toNeighbour(V, E):
    graph = [[] for _ in range(V)]
    for (x, y, _) in E:
        graph[x-1].append([y-1, 1])
        graph[y-1].append([x-1, 1])
    return graph


def maxFlowBFS(V, E, s=0, t=_sentinel):
    if t is _sentinel:
        t = V - 1
    graph = toNeighbour(V, E)
    flow = 0

    def augumentingPath():
        nonlocal V, graph, s, t
        size = [True] + [False] * (V-1)
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
                return path
            for neighbour, capacity in graph[vertex]:
                if not size[neighbour] and capacity:
                    size[neighbour] = True
                    parent[neighbour] = vertex
                    que.put(neighbour)
        return None

    path = augumentingPath()
    while path:
        flow += 1
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for j, (neighbour, _) in enumerate(graph[u]):
                if neighbour == v:
                    graph[u][j][1] = 0
                    break
            for j, (neighbour, _) in enumerate(graph[v]):
                if neighbour == u:
                    graph[v][j][1] = 1
                    break
        path = augumentingPath()
    return flow

def otocz(V, E):
    mini = float("inf")
    for i in range(1, V):
        mini = min(mini, maxFlowBFS(V, E, 0, i))
    return mini


def Optimal(V, E):
    return len(min(toNeighbour(V, E), key=lambda x: len(x)))

if __name__ == "__main__":
    #runtests(Optimal)
    runtests(otocz)
