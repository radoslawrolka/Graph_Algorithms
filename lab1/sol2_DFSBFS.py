from test import runtests
from queue import Queue
from collections import deque
from sys import setrecursionlimit
setrecursionlimit(100000)

def toNeighbour(V, E):
    graph = [[] for _ in range(V)]
    for (x, y, c) in E:
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    return graph


def DFS_array(V, graph):
    visited = [False for _ in range(V)]
    visited[0] = True

    que = deque()
    que.append(0)

    while que:
        vertex = que.pop()
        if vertex == 1:
            return True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                que.append(neighbour)
    return visited[1]

def BFS_array(V, graph, start=0):
    visited = [False for _ in range(V)]
    visited[start] = True

    que = Queue()
    que.put(start)

    while not que.empty():
        vertex = que.get()
        if vertex == 1:
            return True
        for neighbour in graph[vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                que.put(neighbour)
    return visited[1]

def maxmin_edgeval_DFS(V, E):
    left = 0
    right = len(E) - 1
    E.sort(key=lambda x: x[2])
    saved = 0
    while left <= right:
        mid = (left + right) // 2
        if DFS_array(V, toNeighbour(V, E[mid:])):
            saved = E[mid][2]
            left = mid + 1
        else:
            right = mid -1

    return saved

def maxmin_edgeval_BFS(V, E):
    left = 0
    right = len(E) - 1
    E.sort(key=lambda x: x[2])
    saved = 0
    while left <= right:
        mid = (left + right) // 2
        if BFS_array(V, toNeighbour(V, E[mid:])):
            saved = E[mid][2]
            left = mid + 1
        else:
            right = mid -1

    return saved

if __name__ == "__main__":
    runtests(maxmin_edgeval_DFS)
    #runtests(maxmin_edgeval_BFS)
