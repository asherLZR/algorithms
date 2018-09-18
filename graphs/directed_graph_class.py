class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return f"({self.u}, {self.v}, {self.w})"

class DirectedGraph:
    def __init__(self, n):
        self.adj_list = [[] for _ in range(n)]

    def add(self, u, v, w):
        # noinspection PyTypeChecker
        self.adj_list[u].append(Edge(u, v, w))

    def __str__(self):
        return "\n".join([str(i) + ": " + ", ".join(str(e) for e in e_list) for i, e_list in enumerate(self.adj_list)])

if __name__ == '__main__':
    n_vertices = 4
    edges = [(0, 1, 10), (1, 2, 20), (3, 2, 40), (0, 3, 30)]
    g = DirectedGraph(n_vertices)
    for v1, v2, weight in edges:
        g.add(v1, v2, weight)
    print(g)