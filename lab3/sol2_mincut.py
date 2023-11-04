from test import runtests
from queue import PriorityQueue

class Node:
    def __init__(self):
        self.edges = {}
        self.merged = []

    def addEdge(self, to, capacity):
        self.edges[to] = self.edges.get(to, 0) + capacity

    def delEdge(self, to):
        del self.edges[to]

    def merge(self, other):
        self.merged += other


def toNeighbour(V, E):
    G = [Node() for _ in range(V)]
    for x, y, c in E:
        G[x-1].addEdge(y-1, c)
        G[y-1].addEdge(x-1, c)
    return G


def mergeVertices(G, x, y):
    for neighbour, capacity in G[y].edges.items():
        if neighbour == x:
            G[neighbour].delEdge(y)
            G[neighbour].merge(G[y].merged + [y])
            continue
        G[x].addEdge(neighbour, capacity)
        G[neighbour].addEdge(x, capacity)
        G[neighbour].delEdge(y)


def minimumCutPhase(G, V, a=0):
    S = [a]
    que = PriorityQueue()
    que.put((0, a))
    visited = [False] * len(G)
    capacity = [0] * len(G)
    while not que.empty():
        cap, vertex = que.get()
        if not visited[vertex]:
            S.append(vertex)
            visited[vertex] = True
            for neighbour, c in G[vertex].edges.items():
                if not visited[neighbour]:
                    capacity[neighbour] += c
                    que.put((-capacity[neighbour], neighbour))
    s = S[-1]
    t = S[-2]
    result = 0
    for _, c in G[s].edges.items():
        result += c
    mergeVertices(G, t, s)
    return result, G[s].merged+[s]

"""easier to understand, but slower
def minimumCutPhase(G, V, a=0):
    S = [a]
    visited = [False] * len(G)
    visited[a] = True
    while len(S) != V:
        maxsum = (-1, -1)
        for x in range(len(G)):
            if visited[x]:
                continue
            sum = 0
            for y, c in G[x].edges.items():
                if y in S:
                    sum += c
            if sum > maxsum[0]:
                maxsum = (sum, x)
        S.append(maxsum[1])
        visited[maxsum[1]] = True

    s = S[-1]
    t = S[-2]
    result = 0
    for v, c in G[s].edges.items():
        result += c
    mergeVertices(G, t, s)
    return result
"""

def stoer_wagner_algorithm(V, E):
    G = toNeighbour(V, E)
    result = float('inf')
    cuts = None
    for i in range(V-1):
        res, cut = minimumCutPhase(G, V-i)
        if res < result:
            result = res
            cuts = cut
    #cutsB = [i for i in range(V) if i not in cuts]
    #print((cuts, cutsB))
    #return result, (cuts, cutsB)
    return result


if __name__ == "__main__":
    runtests(stoer_wagner_algorithm)
