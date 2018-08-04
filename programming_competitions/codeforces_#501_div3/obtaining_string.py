n = int(input())
s = list(input())
t = list(input())

sw = 0
so = []
for i in range(n):
    f = True
    if s[i] != t[i]:
        found = None
        for j in range(i, n):
            if s[j] == t[i]:
                found = j
                break
        if found is not None:
            for k in range(found, i, -1):
                s[k], s[k-1] = s[k-1], s[k]
                so.append(k)
        else:
            f = False
    if not f:
        break
if s != t:
    print(-1)
else:
    print(len(so))
    for e in so:
        print(e, end=" ")