n, k = map(int, input().split())
a = list(map(int, input().split()))

a_s = sorted(enumerate(a), key=lambda x: x[1], reverse=True)
a_s2 = sorted(a_s[:k], key=lambda x: x[0])
ac = 0
b = []
first = True
p = 0
val = 0
if k > 1:
    for i, j in a_s2:
        if not first:
            b.append(i - p)
            p = i
        else:
            first = False
        ac += j
        val = i
else:
    ac = a_s2[0][1]
b.append(n - val)
print(ac)
print(' '.join(map(str, b)))
