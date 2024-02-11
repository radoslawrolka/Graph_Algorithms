from data import runtests
from collections import defaultdict
from queue import Queue

def to_adjacency_list(E, entry):
    adj = defaultdict(list)
    for u, v in E:
        if u == entry or v == entry:
            continue
        adj[u].append(v)
        adj[v].append(u)
    return adj
        
def build_from_path(path):
    subgraph = defaultdict(list)
    current = 0
    prev = []
    length = 1
    for i in path:
        if i == '+':
            subgraph[current].append(length)
            subgraph[length].append(current)
            prev.append(current)
            current = length
            length += 1
        elif i == '^':
            current = prev.pop()
        else:
            prev.append(current)
            x = int(i)
            if len(subgraph[current]) <= x:
                current = subgraph[current][-1]
            else:
                current = subgraph[current][x]
    return subgraph

def bfs(graph, start=0):
    result = []
    distance = defaultdict(lambda: [])
    distance[start].append(len(graph[start]))

    que = Queue()
    que.put(start)
    while not que.empty():
        vertex = que.get()
        flag = False
        for neighbour in graph[vertex]:
            if not distance[neighbour]:
                flag = True
                distance[neighbour] += distance[vertex] + [len(graph[neighbour])]
                que.put(neighbour)
        if not flag:
            result.append(distance[vertex])
    return result

def solution(_, entry, E, path):
    graph = to_adjacency_list(E, entry)
    subgraph = build_from_path(path.split())
    subbfs = bfs(subgraph)
    for v in graph.keys():
        orgbfs = bfs(graph, v)
        for a in subbfs:
            flag = False
            length = len(orgbfs)
            i = 0
            while i < length:
                if len(a) > len(orgbfs[i]):
                    orgbfs.pop(i)
                    length -= 1
                else:
                    for j in range(len(a)):
                        if a[j] > orgbfs[i][j]:
                            i += 1
                            break
                    else:
                        flag = True
                        orgbfs.pop(i)
                        break
            if not flag:
                break
        else:
            return True
    return False


runtests(solution)
