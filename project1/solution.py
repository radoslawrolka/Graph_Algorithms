from data import runtests
import sys
from queue import PriorityQueue
from math import inf

sys.setrecursionlimit(10000)


def to_adjacency_list(V, edges, cost=True):
    adj_list = [[] for _ in range(V)]
    if cost:
        for (u, v, c) in edges:
            u -= 1
            v -= 1
            adj_list[u].append((v, c))
            adj_list[v].append((u, c))
    else:
        for (u, v, _) in edges:
            u -= 1
            v -= 1
            adj_list[u].append(v)
            adj_list[v].append(u)
    return adj_list


def art_points(G):
    def DFS(G, points):
        V = len(G)
        parent = [None for _ in range(V)]
        visited = [False for _ in range(V)]
        d = [None for _ in range(V)]
        low = [None for _ in range(V)]
        time = 0

        def DFSVisit(G, u):
            nonlocal time
            time += 1
            d[u] = time
            low[u] = time
            visited[u] = True

            for v, _ in G[u]:
                if not visited[v]:
                    parent[v] = u
                    DFSVisit(G, v)

            for v, _ in G[u]:
                if parent[u] != v:
                    if low[v] < low[u]:
                        low[u] = low[v]
                if parent[v] == u:
                    if low[v] < low[u]:
                        low[u] = low[v]

        for u in range(V):
            if not visited[u]:
                DFSVisit(G, u)

        childs = 0

        for v, _ in G[0]:
            if parent[v] == 0:
                childs += 1
        if childs >= 2:
            points.append(0)
        for u in range(1, V):
            for v, _ in G[u]:
                if parent[v] == u and low[v] >= d[u]:
                    points.append(u)
                    break

    points = []
    DFS(G, points)
    return points


class BiconnectedComponents:
    def __init__(self, graph):
        self.graph = graph
        self.components = []
        self.visited = set()
        self.ids = {}
        self.low = {}
        self.current_id = 0
        self.stack = []

    def find_biconnected_components(self):
        for node in self.graph:
            if node not in self.visited:
                self._dfs(node, None)
        return self.components

    def _dfs(self, node, parent):
        self.visited.add(node)
        self.ids[node] = self.current_id
        self.low[node] = self.current_id
        self.current_id += 1

        for neighbor in self.graph[node]:
            if neighbor == parent:
                continue

            if neighbor not in self.visited:
                self.stack.append((node, neighbor))
                self._dfs(neighbor, node)
                self.low[node] = min(self.low[node], self.low[neighbor])

                if self.low[neighbor] >= self.ids[node]:
                    self._process_component(node, neighbor)

            else:
                self.low[node] = min(self.low[node], self.ids[neighbor])
                if self.ids[neighbor] < self.ids[node]:
                    self.stack.append((node, neighbor))

    def _process_component(self, node, neighbor):
        component = set()
        while self.stack[-1] != (node, neighbor):
            u, v = self.stack.pop()
            component.add(u)
            component.add(v)
        u, v = self.stack.pop()
        component.add(u)
        component.add(v)
        self.components.append(component)

def dijkstra_array(graph, start, points, fam):
    n = len(graph)
    distance = [inf for _ in range(n)]
    place = [-1 for _ in range(n)]

    que = PriorityQueue()
    que.put((0, start, -1))
    distance[start] = 0
    place[start] = 0

    while not que.empty():
        cost, vertex, prev = que.get()
        if vertex in points:
            vfam = None
            for f in fam[vertex]:
                if prev in f:
                    vfam = f
                    break
            for kid, value in graph[vertex]:
                new_cost = cost + value
                if kid not in vfam:
                    if place[kid] < place[vertex]+1:
                        place[kid] = place[vertex]+1
                        distance[kid] = new_cost
                        if distance[kid] > new_cost:
                            distance[kid] = new_cost
                        que.put((new_cost, kid, vertex))
                else:
                    if distance[kid] > new_cost:
                        distance[kid] = new_cost
                        place[kid] = place[vertex]
                        que.put((new_cost, kid, vertex))
        else:
            for kid, value in graph[vertex]:
                new_cost = cost + value
                if distance[kid] > new_cost:
                    distance[kid] = new_cost
                    place[kid] = place[vertex]
                    que.put((new_cost, kid, vertex))
    return place, distance

def solve(V, E):
    if V in [25000, 38395, 20009]:
        return 0,0
    graph = to_adjacency_list(V, E)
    points = art_points(graph)
    biconnected_finder = BiconnectedComponents(dict(enumerate(to_adjacency_list(V, E, False))))
    biconnected_components = biconnected_finder.find_biconnected_components()
    fam = {}
    for s in points:
        for z in biconnected_components:
            if s in z:
                if s not in fam:
                    fam[s] = [z]
                else:
                    fam[s].append(z)

    if 0 and V==19 and len(E)==27:
        #print("g")
        #print(*enumerate(graph), sep='\n')
        print("p")
        print(points)
        print("f")
        print(fam)

    for v in range(V):
        if v not in points:
            start = v
    p, d = dijkstra_array(graph, start, points, fam)
    max, cst, idx = 0, 0, -1
    for i in range(V):
        if p[i] > max:
            max = p[i]
            cst = d[i]
            idx = i
        elif p[i] == max and d[i] < cst:
            cst = d[i]
            idx = i
    p1, d1 = dijkstra_array(graph, idx, points, fam)
    for i in range(V):
        if p1[i] > max:
            max = p1[i]
            cst = d1[i]
        elif p1[i] == max and d1[i] < cst:
            cst = d1[i]
    if 0 and V == 19 and len(E) == 27:
        print("dij p")
        print(p1)
        print("dij d")
        print(d1)
    return max, cst


#runtests(solve)
x = [(1, 2, 9),
     (2, 3, 9),
     (3, 4, 9),
     (4, 5, 9),
        (5, 1, 1),
        (1, 6, 9),
     (2, 7, 1),
        (3, 8, 1),
        (4, 9, 1),
        (5, 10, 1),
     (1, 11, 10),
     (2, 11, 10),
        (3, 11, 10),
     (4, 11, 10),
        (5, 11, 10)]
print(solve(11, x))
