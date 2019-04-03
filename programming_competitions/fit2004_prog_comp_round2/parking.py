n = int(input())
a = list(map(int, input().split()))

a.sort()
r = 0
c = 0

for i in a:
    if r <= i:
        r += i
        c += 1
print(c)
