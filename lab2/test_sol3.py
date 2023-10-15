from os import listdir
from dimacs import *

def runtests(func):
    flag = True
    for f in listdir("connectivity"):
        (V, E) = loadDirectedWeightedGraph("connectivity/"+f)
        print(f, end=" |")
        res = func(V, E)
        sol = readSolution("connectivity/"+f)
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
