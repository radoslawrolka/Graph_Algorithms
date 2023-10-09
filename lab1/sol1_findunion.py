from test import runtests


class FindUnion:
    def __init__(self, num_of_vertices):
        self.parent = [_ for _ in range(num_of_vertices)]
        self.rank = [0 for _ in range(num_of_vertices)]

    def find_root(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_root(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[y_root] += 1
        return True


def Kruksal_MST_object(num_of_vertices, graph):
    MST = []
    maxmin_cost = float("inf")

    fin_uni_obj = FindUnion(num_of_vertices+1)
    graph.sort(key=lambda x: x[2], reverse=True)
    for v_1, v_2, cost in graph:
        added_edge = fin_uni_obj.union(v_1, v_2)
        if added_edge:
            MST.append((v_1, v_2))
            if fin_uni_obj.find_root(1) == fin_uni_obj.find_root(2):
                maxmin_cost = cost
                break
    return maxmin_cost

if __name__ == "__main__":
    runtests(Kruksal_MST_object)
