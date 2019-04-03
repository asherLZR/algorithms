n = int(input())
a = list(map(int, input().split(" ")))
a.sort()
m = 0
e = [0]*6
prev = n
for i in range(n-1, -1, -1):
    if prev != n and a[prev] - a[i] <= 5:
        diff = a[prev] - a[i]
        e = [0]*diff + e[:6-diff]
        if e[-1] > 0:
            e[-1] -= 1
    else:
        e = [0] * 6
        # print(a[i], a[prev], diff, e[:6-diff])
    curr = i
    for k in range(6):
        if a[i]-k >= 0 and a[i]-k == a[curr]:
            e[5-k] += 1
            if e[5-k] > m:
                m = e[5-k]
            curr -= 1
    prev -= 1
    # print(e)
print(m)

n = int(input())
a = list(map(int, input().split(" ")))
a.sort()
m = 0
d = [0]*(max(a)+1)
prev = n-1
for i in range(n-1, -1, -1):
    if prev != n-1 and a[prev] - a[i] <= 5:
        diff = a[prev] - a[i]
    for k in range(6):
        if a[i]-k >= 0:
            d[a[i]-k] += 1
            if d[a[i]-k] > m:
                m = d[a[i]-k]
    prev -= 1
print(m)
#
