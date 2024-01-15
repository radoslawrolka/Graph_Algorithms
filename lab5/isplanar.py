import networkx as nx
from networkx.algorithms.planarity import check_planarity
from test import runtests

def is_planar(V, E):
    G = nx.Graph()
    for a, b, _ in E:
        G.add_edge(a, b)
    return 1 if check_planarity(G)[0] else 0

runtests("plnar", is_planar, isDirected=False)
