from queue import Queue


def bfs(n, m, E, s):
    E = sorted(E, key=lambda x: (x[0], x[1]))

    adj_list = {}
    for i in range(1, n+1):
        adj_list[i] = set()
    for u, v in E:
        adj_list[u].add(v)
        adj_list[v].add(u)

    Q = Queue()
    Q.put(s)
    F = [-1] * (n+1)
    F[s] = 0
    while not Q.empty():
        chosen = Q.get()
        for adj_v in adj_list[chosen]:
            if F[adj_v] == -1:
                F[adj_v] = F[chosen] + 6
                Q.put(adj_v)
    return F[1:s] + F[s+1:]


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)
        print(' '.join(map(str, result)))
