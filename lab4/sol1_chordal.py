from test import runtests

class Node:
    def __init__(self, idx):
        self.idx = idx     # indeks
        self.out = set()   # zbiór sąsiadów
        self.parent = None # najpóźniej pojawiający się element RN(v)
        self.RN = set()    # zbiór sąsiadów pojawiających się wcześniej w wyniku lexBFS niż v

    def connect_to(self, v):
        self.out.add(v)


def toNeighbour(V, E):
    G = [None] + [Node(i) for i in range(1, V + 1)]
    for (u, v, _) in E:
        G[u].connect_to(v)
        G[v].connect_to(u)
    return G


def lexBFS(G):
    visited = []                        # lista odwiedzonych wierzchołków
    vertices = [set(range(1, len(G)))]  # lista leksykograficznie uporządkowanych zbiorów wierzchołków
    for _ in range(len(G)-1):           # aby wszystkie wierzchołki były w liście visited
        current = vertices[-1].pop()    # aktualnie przetwarzany wierzchołek
        visited.append(current)
        idx = 0
        while idx < len(vertices):      # aktualizacja listy uporządkowanych zbiorów wierzchołków
            i = 0
            neighbours = G[current].out & vertices[idx]  # sąsiedzi z najaktualniejszego zbioru
            not_neighbours = vertices[idx] - neighbours  # dopełnienie
            if len(neighbours) > 0:                      # wstawianie najaktualniejszego zbioru
                vertices.insert(idx+1, neighbours)
                i += 1
            if len(not_neighbours) > 0:
                vertices.insert(idx+1, not_neighbours)  # wstawianie przed najaktualniejszy zbiór
                i += 1
            vertices.remove(vertices[idx])              # usunięcie bazowego (wykorzystanego) zbioru
            idx += i
        G[current].RN = set(visited) & G[current].out   # aktualizacja RN dla wierzchołka current
        parentsearch = visited.copy()                   # aktualizacja parenta dla wierzchołka current
        while parentsearch and not ({parentsearch[-1]} & G[current].RN):
            parentsearch.pop()
        if parentsearch:
            G[current].parent = parentsearch[-1]
    return visited


# sprawdza czy lexBFS działa poprawnie
def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True


# Z definicji kolejności idealnej eliminacji, zbiór RN(v) + {v} powinien być kliką,
# więc w szczególności:
# RN(v) poza parent(v) powinien zawierać się w RN(parent(v)).
def PEO(V, E):
    graph = toNeighbour(V, E)
    order = lexBFS(graph)
    print("", checkLexBFS(graph, order), end=" | ")
    for v in order[1:]:
        if not graph[v].RN - {graph[v].parent} <= graph[graph[v].parent].RN:
            return 0
    return 1


if __name__ == '__main__':
    print("filename // checkLexBFS // PEO")
    runtests("chordal", PEO, isDirected=False)
