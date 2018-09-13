a = "WOOLLOOMOOLOO$"
b = []
for _ in range(len(a)):
    b.append(a)
    a = a[-1] + a[:-1]

for w in sorted(b):
    print(w)