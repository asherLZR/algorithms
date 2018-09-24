import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    adj_list = {}
    for i in range(1, n + 1):
        adj_list[i] = set()
    for _ in range(m):
        a, b, w = map(int, sys.stdin.readline().split())
        adj_list[a].add((b, w))
        adj_list[b].add((a, w))
    s = int(input())

