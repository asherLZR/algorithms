import queue
import math
import copy

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return f"({self.u}, {self.v}, {self.w})"

class Vertex:
    def __init__(self, u):
        self.id = u
        self.discovered = False
        self.cost = math.inf
        self.previous = None
        self.finalised = False

    def __str__(self):
        return str(self.id)

class DirectedGraph:
    def __init__(self, n):
        self.vertices = [Vertex(x) for x in range(n)]
        self.adj_list = [[] for _ in range(n)]

    def add(self, u, v, w):
        # noinspection PyTypeChecker
        self.adj_list[u].append(Edge(self.vertices[u], self.vertices[v], w))

    def __str__(self):
        return "\n".join([str(i) + ": " + ", ".join(str(e) for e in e_list) for i, e_list in enumerate(self.adj_list)])


n, m = map(int, input().split())
g = DirectedGraph(n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    # if w == 0:
    #     w = 1
    # else:
    #     w = 0
    g.add(u, v, w)
    g.add(v, u, w)
finalised = [False] * (n+1)
q_0 = queue.Queue()
q_1 = queue.Queue()
g.vertices[1].cost = 0
q_0.put(g.vertices[1])
while not q_0.empty() or not q_1.empty():
    if not q_0.empty():
        current = q_0.get()
    else:
        current = q_1.get()
    if not current.finalised:
        for e in g.adj_list[current.id]:
            new_d = current.cost + e.w
            if not e.v.finalised and new_d < e.v.cost:
                e.v.cost = new_d
                e.v.previous = e.u
            q_0.put(e.v)
            new_v = copy.deepcopy(e.v)
            new_v.w = 1
            q_1.put(new_v)
        current.finalised = True
    if g.vertices[n].finalised:
        break

current = g.vertices[n]
path = []
while current is not None:
    print(current, current.cost)
    current = current.previous