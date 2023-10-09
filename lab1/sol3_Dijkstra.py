from test import runtests
from queue import PriorityQueue


def dijkstra_array(V, E, start=0, end=1):
    def toNeighbour(V, E):
        graph = [[] for _ in range(V)]
        for (x, y, c) in E:
            graph[x - 1].append((y - 1, c))
            graph[y - 1].append((x - 1, c))
        return graph

    graph = toNeighbour(V, E)
    distance = [0 for _ in range(V)]
    distance[0] = float("inf")

    que = PriorityQueue()
    que.put((-distance[0], start))

    while not que.empty():
        cost, vertex = que.get()
        if vertex == end:
            break
        for kid, value in graph[vertex]:
            new_val = min(value, distance[vertex])
            if distance[kid] < new_val:
                distance[kid] = new_val
                que.put((-new_val, kid))
    return distance[end]

if __name__ == "__main__":
    runtests(dijkstra_array)
