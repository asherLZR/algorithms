a = input()
p, r = a[0], 1
x = "NO"
for i in range(1, len(a)):
    if a[i] == p:
        r += 1
    else:
        p = a[i]
        r = 1
    if r >= 7:
        x = "YES"
        break
print(x)