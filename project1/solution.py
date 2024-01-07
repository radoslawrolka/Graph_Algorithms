from data import runtests
import sys
from queue import PriorityQueue
from math import inf
from queue import Queue
from collections import defaultdict

sys.setrecursionlimit(1000000)
import resource as rc
rc.setrlimit(rc.RLIMIT_STACK, (rc.RLIM_INFINITY, rc.RLIM_INFINITY))




def solve(V, E):
    def to_adjacency_list():
        for (u, v, c) in E:
            u -= 1
            v -= 1
            graph[u].append((v, c))
            graph[v].append((u, c))

    def Dikstra_roll(graph, art, fam):
        result = defaultdict(list)
        visited = [False for _ in range(len(graph))]

        que = PriorityQueue()
        artq = Queue()
        i = art.pop()
        art.add(i)
        artq.put((0, i))

        while not artq.empty():
            a, b = artq.get()
            father = b
            que.put((a, b))
            while not que.empty():
                cost, vertex = que.get()
                visited[vertex] = True
                for kid, value in graph[vertex]:
                    if visited[kid]: continue
                    if kid in art:
                        artq.put((0, kid))
                        result[kid].append((father, cost + value))
                        result[father].append((kid, cost + value))
                    else:
                        que.put((cost + value, kid))
        for f in fam.values():
            for s in f:
                flag = 0
                a = None
                for v in s:
                    if v in art:
                        flag += 1
                        a = v
                        if flag == 2:
                            break
                if flag == 1:
                    minic = inf
                    ver = None
                    for v, c in graph[a]:
                        if v in s and c < minic:
                            minic = c
                            ver = v
                    result[a].append((ver, minic))
                    result[ver].append((a, minic))
        return result

    def art_points():
        parent = [None for _ in range(V)]
        visited = [False for _ in range(V)]
        d = [None for _ in range(V)]
        low = [None for _ in range(V)]
        time = 0
        points = set()

        def DFSVisit(u):
            nonlocal time
            time += 1
            d[u] = time
            low[u] = time
            visited[u] = True
            for v, _ in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    DFSVisit(v)

            for v, _ in graph[u]:
                if parent[u] != v:
                    if low[v] < low[u]:
                        low[u] = low[v]
                if parent[v] == u:
                    if low[v] < low[u]:
                        low[u] = low[v]

        for u in range(V):
            if not visited[u]:
                DFSVisit(u)

        childs = 0
        for v, _ in graph[0]:
            if parent[v] == 0:
                childs += 1
        if childs >= 2:
            points.add(0)
        for u in range(1, V):
            for v, _ in graph[u]:
                if parent[v] == u and low[v] >= d[u]:
                    points.add(u)
                    break
        return points

    def find_biconnected_components1():
        components = []
        visited = set()
        ids = {}
        low = {}
        current_id = 0
        stack = []
        points = set()
        parentlist = {}
        parentlist[0] = None

        def _dfs(node, parent):
            nonlocal current_id
            visited.add(node)
            ids[node] = current_id
            low[node] = current_id
            current_id += 1

            for neighbor, _ in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor not in visited:
                    stack.append((node, neighbor))
                    parentlist[neighbor] = node
                    _dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])

                    if low[neighbor] >= ids[node]:
                        _process_component(node, neighbor)

                else:
                    low[node] = min(low[node], ids[neighbor])
                    if ids[neighbor] < ids[node]:
                        stack.append((node, neighbor))

        def _process_component(node, neighbor):
            component = set()
            while stack[-1] != (node, neighbor):
                u, v = stack.pop()
                component.add(u)
                component.add(v)
            u, v = stack.pop()
            component.add(u)
            component.add(v)
            components.append(component)

        for node in range(len(graph)):
            if node not in visited:
                _dfs(node, None)

        childs = 0
        for v, _ in graph[0]:
            if parentlist[v] == 0:
                childs += 1
        if childs >= 2:
            points.add(0)
        for u in range(1, V):
            for v, _ in graph[u]:
                if parentlist[v] == u and low[v] >= ids[u]:
                    points.add(u)
                    break

        rescomp = defaultdict(list)
        for c in components:
            for p in points:
                if p in c:
                    rescomp[p].append(c)
        return rescomp, points

    def find_biconnected_components():
        components = {}
        for p in points:
            components[p] = []
        visited = set()
        ids = {}
        low = {}
        current_id = 0
        stack = []

        def _dfs(node, parent):
            nonlocal current_id
            visited.add(node)
            ids[node] = current_id
            low[node] = current_id
            current_id += 1

            for neighbor, _ in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor not in visited:
                    stack.append((node, neighbor))
                    _dfs(neighbor, node)
                    low[node] = min(low[node], low[neighbor])

                    if low[neighbor] >= ids[node]:
                        _process_component(node, neighbor)

                else:
                    low[node] = min(low[node], ids[neighbor])
                    if ids[neighbor] < ids[node]:
                        stack.append((node, neighbor))

        def _process_component(node, neighbor):
            component = set()
            while stack[-1] != (node, neighbor):
                u, v = stack.pop()
                component.add(u)
                component.add(v)
            u, v = stack.pop()
            component.add(u)
            component.add(v)
            for p in points:
                if p in component:
                    components[p].append(component)

        for node in range(len(graph)):
            if node not in visited:
                _dfs(node, None)
        return components

    def dijkstra_array(start, breaker):
        distance = [inf for _ in range(V)]
        place = [-1 for _ in range(V)]
        visited = [False for _ in range(V)]

        que = PriorityQueue()
        que.put((0, start, -1))
        distance[start] = 0
        place[start] = 0

        while not que.empty():
            cost, vertex, prev = que.get()
            visited[vertex] = True
            if cost > breaker: break
            if vertex in points:
                vfam = None
                for f in fam[vertex]:
                    if prev in f:
                        vfam = f
                        break
                for kid, value in graph[vertex]:
                    if visited[kid]: continue
                    new_cost = cost + value
                    if kid not in vfam:
                        if True:
                            place[kid] = place[vertex] + 1
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
                    if visited[kid]: continue
                    new_cost = cost + value
                    if distance[kid] > new_cost:
                        distance[kid] = new_cost
                        place[kid] = place[vertex]
                        que.put((new_cost, kid, vertex))
        return place, distance

    graph = [[] for _ in range(V)]
    to_adjacency_list()
    #points = art_points()
    fam, points = find_biconnected_components1()
    mem = {}

    for v in range(V):
        if v not in points:
            start = v
    p, d = dijkstra_array(start, inf)
    newstart = []
    max = 0
    for i in range(V):
        if p[i] > max:
            max = p[i]
            newstart = [i]
        elif p[i] == max:
            newstart.append(i)
    max, cst = 0, inf
    for idx in newstart:
        p1, d1 = dijkstra_array(idx, cst)
        for i in range(V):
            if p1[i] > max:
                max = p1[i]
                cst = d1[i]
            elif p1[i] == max and d1[i] < cst:
                cst = d1[i]

    return max, cst


runtests(solve)
