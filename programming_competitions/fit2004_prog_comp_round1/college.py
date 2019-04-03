def euclid_gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

t = int(input())
for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    gcd = ar[0]
    for e in ar:
        gcd = euclid_gcd(gcd, e)
    ac = 0
    for e in ar:
        ac += e//gcd
    print(str(gcd) + " " + str(ac))