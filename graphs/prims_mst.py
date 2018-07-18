import random

n, m = map(int, input().split())
adj_list = {}
for i in range(1, n+1):
    adj_list[i] = set()
for _ in range(m):
    a, b, w = map(int, input().split())
    adj_list[a].add((b, w))
    adj_list[b].add((a, w))
r = int(input())

# the minimum cost to reach a vertex and the edge providing that minimum cost
C, E = [float('inf')] * (n+1), [None] * (n+1)
# all undiscovered vertices, to be removed once chosen
U = [x+1 for x in range(n)]
# the forest to be built up
T = []
mst_cost = 0
C[random.choice(U)] = 0

while U:
    # choose a vertex by the lowest cost in C
    chosen, c_cost = min(enumerate(C), key=lambda x: x[1])
    # once it has been chosen, its cost returns to infinity to prevent is from being chosen as a future min
    C[chosen] = float('inf')
    # the vertex has now been chosen so no longer consider returning to it when looking at future edges
    U.remove(chosen)
    mst_cost += c_cost
    # build the tree with the chosen vertex and edge if it exists
    if E[chosen] is not None:
        T.append(E[chosen])
    # for every adjacent vertex to chosen
    for v, w in adj_list[chosen]:
        # adjacent edge is incident to an unvisited vertex and its weight is less than a previously found edge
        if v in U and w < C[v]:
            # update cost of adjacent vertex
            C[v] = w
            E[v] = (chosen, v, w)

print(mst_cost)
print(T)
