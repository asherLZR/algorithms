n, q = map(int, input().split())
s = list(map(int, input().split()))
a_l = {}
for i in range(1, n+1):
    a_l[i] = []
for i, e in enumerate(s):
    ind = i + 2
    a_l[e].append(ind)
for k, v in a_l.items():
    a_l[k] = sorted(v)
o = [-1 for x in range(n+1)]
ct = 1

st = [1]
while st:
    c = st[-1]
    if o[c] == -1:
        o[c] = ct
        ct += 1
    if a_l[c]:
        d = a_l[c].pop(0)
        st.append(d)
    else:
        st.pop(-1)
print(sorted(enumerate(o), key=lambda x: x[1]))

for _ in range(q):
    o = o[1:]
    u, k = map(int, input().split())
    print()
