from os import listdir
from dimacs import *

def runtests(folder, func, isDirected=False, isCNFF=False, ommit=None):
    if ommit is None:
        ommit = []
    flag = True
    for f in listdir(folder):
        if f in ommit:
            continue
        if isDirected:
            (V, E) = loadDirectedWeightedGraph(f"{folder}/{f}")
        elif isCNFF:
            (V, E) = loadCNFFormula(f"{folder}/{f}")
        else:
            (V, E) = loadWeightedGraph(f"{folder}/{f}")
        print(f"{f:<19}", end=" |")
        res = func(V, E)
        sol = readSolution(f"{folder}/{f}")
        if str(res) == sol:
            print("OK")
        else:
            print("Wrong answer")
            print("Your answer:", res)
            print("Correct answer:", sol)
            flag = False
            break
    if flag:
        print("All tests passed")
        return True
    else:
        return False
