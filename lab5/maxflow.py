import networkx as nx
from networkx.algorithms.flow import maximum_flow
from test import runtests

def maxflow(V, E):
    G = nx.DiGraph()
    for a, b, c in E:
        G.add_edge(a, b, capacity=c)
    return maximum_flow(G, 1, V)[0]


runtests("flow", maxflow, isDirected=True)
