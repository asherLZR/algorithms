a = input().strip().replace(" ", "")
b = input().strip().replace(" ", "")
d = {}
for l in a:
    if l not in d:
        d[l] = 1
    else:
        d[l] += 1
f = True
for l in b:
    if l not in d or d[l] <= 0:
        f = False
        break
    else:
        d[l] -= 1
if f:
    print("YES")
else:
    print("NO")
