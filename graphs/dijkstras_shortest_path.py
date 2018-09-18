import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    adj_list = {}
    for i in range(1, n+1):
        adj_list[i] = set()
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        adj_list[a].add((b, w))
        adj_list[b].add((a, w))
    s = int(input())

    # cost of visiting vertex given by index
    C = [float('inf')] * (n+1)
    # unvisited vertices are marked with False
    U = [False for _ in range(n+1)]
    # final costs from source to all other vertices, -1 means not reachable
    F = [-1] * (n+1)
    C[s] = 0

    for _ in range(n):
        # replace this with a min heap
        chosen, c_weight = min(enumerate(C), key=lambda x: x[1])
        C[chosen] = float('inf')
        U[chosen] = True
        F[chosen] = c_weight
        for v, w in adj_list[chosen]:
            # v has not been visited and its cost can be relaxed
            if not U[v] and w + c_weight < C[v]:
                C[v] = w + c_weight
    print(' '.join(map(str, F[1:s] + F[s+1:])))
