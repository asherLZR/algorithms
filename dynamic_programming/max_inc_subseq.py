# 0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15

a = list(map(int, input().split()))
memo = [0] * len(a)
memo[0] = 1
for i in range(len(a)):
    prev = [x for j, x in enumerate(memo[:i]) if a[i] > a[j]]
    if len(prev) > 0:
        memo[i] = 1 + max(prev)
print(max(memo))