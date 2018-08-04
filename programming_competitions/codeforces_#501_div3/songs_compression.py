n, m = map(int, input().split())
s = []
uc = 0
c = 0
for _ in range(n):
    a, b = map(int, input().split())
    s.append((a, b))
    uc += a
t = sorted(s, key=lambda x: x[0]-x[1], reverse=True)
for i in range(n):
    if uc <= m:
        break
    uc -= (t[i][0] - t[i][1])
    c += 1
if uc > m:
    print(-1)
else:
    print(c)
