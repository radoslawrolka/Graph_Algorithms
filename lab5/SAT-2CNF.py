from test import runtests
import networkx as nx
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort


def isCNFFTrueAble(V, E):
    G = nx.DiGraph()
    for a, b in E:
        G.add_edge(-a, b)
        G.add_edge(-b, a)
    SSC = strongly_connected_components(G)
    for ssc in SSC:
        for el in ssc:
            if -el in ssc:
                return "solution=0"
    return "solution=1"


def findCNFF(V, E):
    G = nx.DiGraph()
    for a, b in E:
        G.add_edge(-a, b)
        G.add_edge(-b, a)
    SSC = list(strongly_connected_components(G))
    whichSSC = {}
    for i, ssc in enumerate(SSC):
        for el in ssc:
            whichSSC[el] = i
            if -el in ssc:
                return "solution=0"
    H = nx.DiGraph()
    for i, scc in enumerate(SSC):
        for el in scc:
            for _, dest in G.edges(el):
                if whichSSC[dest] != i:
                    H.add_edge(i, whichSSC[dest])
    order = list(topological_sort(H))
    result = {}
    for i in order:
        for el in SSC[i]:
            if result.get(el) is None:
                result[el] = False
                result[-el] = True

    for a, b in E:
        assert result[a] or result[b]
    # return result
    return "solution=1"


runtests("sat", isCNFFTrueAble, isCNFF=True)
runtests("sat", findCNFF, isCNFF=True)
