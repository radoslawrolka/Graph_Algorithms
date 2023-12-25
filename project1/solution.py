from data import runtests
import sys
sys.setrecursionlimit(1000000)

def to_adjacency_list(V, edges, decrement=False, cost=True):
    adj_list = [[] for _ in range(V)]
    if cost:
        if decrement:
            for (u, v, c) in edges:
                u -= 1
                v -= 1
                adj_list[u].append((v, c))
                adj_list[v].append((u, c))
        else:
            for (u, v, c) in edges:
                adj_list[u].append((v, c))
                adj_list[v].append((u, c))
    else:
        if decrement:
            for (u, v, c) in edges:
                u -= 1
                v -= 1
                adj_list[u].append(v)
                adj_list[v].append(u)
        else:
            for (u, v, c) in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
    return adj_list

def Kruskal_MST_node(graph, num_of_vertices):
    class Node:
        def __init__(self, val):
            self.parent = self
            self.rank = 0
            self.value = val

    def findset(x):
        if x.parent != x:
            x.parent = findset(x.parent)
        return x.parent

    def union(x, y):
        x_root = findset(x)
        y_root = findset(y)
        if x_root == y_root:
            return False
        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        else:
            x_root.parent = y_root
            if x_root.rank == y_root.rank:
                y_root.rank += 1
        return True

    MST = []
    veritces_nodes = [Node(_) for _ in range(num_of_vertices)]
    graph.sort(key=lambda x: x[2])
    for v_1, v_2, cost in graph:
        added_edge = union(veritces_nodes[v_1], veritces_nodes[v_2])
        if added_edge:
            MST.append((v_1, v_2, cost))
    return MST

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
    return set(points)

def dfs_back(graph, points, fam, start):
    global result
    n = len(graph)

    def visit(graph, vertex, prev, first, visited, plac, cost):
        global result
        visited[vertex] = True
        result = max(result, (plac, -cost))
        print(result)
        print(vertex, prev, first, visited, plac, cost)
        for neighbour, c in graph[vertex]:
            if not visited[neighbour]:
                if vertex in points and prev is not None:
                    for el in fam[vertex]:
                        if prev in el:
                            if neighbour in el:
                                visit(graph, neighbour, vertex, first, visited, plac, cost + c)
                            else:
                                visit(graph, neighbour, vertex, first, visited, plac + 1, cost + c)
                            break
                elif vertex in points:
                    visit(graph, neighbour, vertex, neighbour, visited, plac + 1, cost + c)
                else:
                    visit(graph, neighbour, vertex, first, visited, plac, cost + c)

    visit(graph, start, None, None, [False for _ in range(n)], 0, 0)
    return

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

result = (0,0)
def solve(V, E):
    global result
    result = (0,0)
    graph = to_adjacency_list(V, E, True)
    points = art_points(graph)
    biconnected_finder = BiconnectedComponents(dict(enumerate(to_adjacency_list(V, E, True, False))))
    biconnected_components = biconnected_finder.find_biconnected_components()
    for i in range(len(E)):
        E[i] = (E[i][0] - 1, E[i][1] - 1, E[i][2])
    mst = Kruskal_MST_node(E, V)
    mst = to_adjacency_list(V, mst)
    fam = {}
    for s in points:
        for z in biconnected_components:
            if s in z:
                if s not in fam:
                    fam[s] = [z]
                else:
                    fam[s].append(z)
    for s in points:
        dfs_back(mst, points, fam, s)

    print("art points: ", points)
    print("biconnected components: ")
    print(*biconnected_components, sep="\n")
    print("families: ")
    for key in fam:
        print(key, fam[key])
    print("mst: ")
    print(*mst, sep="\n")
    print("result: ")

    return result




#runtests(solve)

e1 = [(1,2,1), (2,3,1), (3,4,9), (3,5,1), (5,6,1), (5,2,9)]
print(solve(6, e1))


