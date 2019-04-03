class Edge:
    def __init__(self, u, v, w, inverted=False):
        self.u = u
        self.v = v
        self.w = w
        self.inverted = inverted

    def __str__(self):
        return f"({self.u}, {self.v}, {self.w})"

class Vertex:
    def __init__(self, u):
        self.id = u
        self.discovered = False
        self.previous = []

    def __str__(self):
        return str(self.id)

class DirectedGraph:
    def __init__(self, n):
        self.vertices = [Vertex(x) for x in range(n)]
        self.adj_list = [[] for _ in range(n)]

    def add(self, u, v, w, inverted=False):
        # noinspection PyTypeChecker
        self.adj_list[u].append(Edge(self.vertices[u], self.vertices[v], w, inverted))

    def get(self, u):
        return self.adj_list[u]

    def __str__(self):
        return "\n".join([str(i) + ": " + ", ".join(str(e) for e in e_list) for i, e_list in enumerate(self.adj_list)])


from queue import Queue

n, m = map(int, input().split())
g = DirectedGraph(n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    g.add(u, v, w)
    g.add(v, u, w, True)
q = Queue()
g.vertices[1].discovered = True
q.put(g.vertices[1])
level = 0
while not q.empty():
    found = False
    for _ in range(q.qsize()):
        current = q.get()
        # print(current, level)
        if current.id == n:
            found = True
        inc_edges = g.get(current.id)
        for e in inc_edges:
            if not e.v.discovered:
                q.put(e.v)
                e.v.discovered = True
            e.v.previous.append(current)
    if found:
        break
    level += 1
for ver in g.vertices[n].previous:
    print(ver)
    pass

# do bfs to find shortest paths of length k - O(V + E) time but space?!
# for each path, find no of incorrect edges
# take the path with min incorrect edges
# for each edge in G, if not in shortest path,