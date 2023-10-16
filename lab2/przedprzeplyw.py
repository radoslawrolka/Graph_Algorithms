# gravity'ish algorithm for finding the maxflow in a graph
# O(V^2 * E)

from test import runtests
_sentinel = object()

class Edge:
    def __init__(self, to, capacity, exist, now=0):
        self.to = to
        self.now = now
        self.capacity = capacity
        self.exist = exist

def toNeighbour(V, E):
    graph = [[] for _ in range(V)]
    matrix = [[None] * V for _ in range(V)]
    for (x, y, c) in E:
        graph[x-1].append(Edge(y-1, c, True))
        graph[y-1].append(Edge(x-1, 0, False))
        matrix[x-1][y-1] = graph[x-1][-1]
        matrix[y-1][x-1] = graph[y-1][-1]
    return graph, matrix

def push_relable(V, E, s=0, t=_sentinel):
    if t is _sentinel:
        t = V - 1
    graph, matrix = toNeighbour(V, E)

    height = [0] * V
    excess = [0] * V
    height[s] = V

    def update_edge(fr, to):
        matrix[fr][to].exist = (matrix[fr][to].now != matrix[fr][to].capacity)

    def can_raise(vertex):
        nonlocal height, excess, graph
        if excess[vertex] <= 0:
            return False
        for e in graph[vertex]:
            if e.exist:
                if height[vertex] > height[e.to]:
                    return False
        return True

    def raise_vertex(vertex):
        nonlocal height, graph
        mini = float('inf')
        for e in graph[vertex]:
            if e.exist:
                mini = min(mini, height[e.to])
        height[vertex] = 1 + mini

    def can_push(vertex, neighbour):
        nonlocal matrix, height, excess
        if excess[vertex] <= 0:
            return False
        if not matrix[vertex][neighbour].exist:
            return False
        if height[vertex] != height[neighbour] + 1:
            return False
        return True

    def push(vertex, neighbour):
        nonlocal graph, excess, matrix
        flow = min(excess[vertex], (abs(matrix[vertex][neighbour].capacity-matrix[vertex][neighbour].now)))
        if matrix[vertex][neighbour].capacity > 0:
            matrix[vertex][neighbour].now += flow
            matrix[neighbour][vertex].now += flow
        else:
            matrix[vertex][neighbour].now -= flow
            matrix[neighbour][vertex].now -= flow
        excess[vertex] -= flow
        excess[neighbour] += flow
        update_edge(vertex, neighbour)
        update_edge(neighbour, vertex)

    def initialize_preflow():
        nonlocal graph, excess, s
        for e in graph[s]:
            flow = e.capacity
            matrix[s][e.to].now = flow
            matrix[e.to][s].now = flow
            excess[e.to] = flow
            excess[s] -= flow
            update_edge(s, e.to)
            update_edge(e.to, s)

    initialize_preflow()
    while True:
        flag = True
        for i in range(1, V-1):
            if can_raise(i):
                raise_vertex(i)
                flag = False
            for e in graph[i]:
                if can_push(i, e.to):
                    push(i, e.to)
                    flag = False
        if flag:
            break

    return excess[t]

if __name__ == '__main__':
    runtests(push_relable)
