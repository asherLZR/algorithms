k = 0 # dont belong to any segment
points = []

n, m = map(int, input().split())
line = [1 for x in range(m+1)]
for _ in range(n):
    l, r = list(map(int, input().split()))
    line[l:r+1] = [0] * (r-l+1)
for i in range(1, m+1):
    if line[i] != 0:
        points.append(i)
        k += 1
print(k)
print(" ".join(map(str, points)))
