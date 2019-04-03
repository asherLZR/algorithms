import math, heapq

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

    def get(self, vertex):
        return self.adj_list[vertex]

    def __str__(self):
        return "\n".join([str(i) + ": " + ", ".join(str(e) for e in e_list) for i, e_list in enumerate(self.adj_list)])

def dijkstras(source):
    min_heap = [(0, source, 0)]
    distance_to = [math.inf] * n
    distance_to[source] = 0
    finalised = [None] * n

    while min_heap:
        current = heapq.heappop(min_heap)
        w, u, _ = current
        if finalised[u] is None:
            for edge in graph.get(u):  # for each edge incident to vertex u
                v, distance_to_v = edge.v, edge.w
                new_distance = distance_to_v + distance_to[u]
                if finalised[v] is None and new_distance < distance_to[v]:
                    distance_to[v] = new_distance
                    heapq.heappush(min_heap, (new_distance, v, u))
            finalised[u] = current
    return distance_to, finalised


def recover(source, target, finalised):
    path = []
    current = target
    while current != source:
        path.append(current)
        edge = finalised[current]
        current = edge[2]
    path.append(source)
    return path[::-1]

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    n += 1
    graph = DirectedGraph(n)
    for _ in range(m):
        u, v, w = map(int, input().strip().split())
        graph.add(u, v, w)
        graph.add(v, u, w)

    dist_st, final_st = dijkstras(1)
    dist_ts, final_ts = dijkstras(n-1)

    min_diff = math.inf
    for i in range(len(dist_st)):
        diff = abs(dist_st[i] - dist_ts[i])
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

