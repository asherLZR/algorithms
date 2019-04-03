# 15 -10 20 8 -30
# 5 -50 100 30 -30 80

import math


a = list(map(int, input().split()))
memo = [a[0]] + [math.inf for _ in range(len(a)-1)]
max_val = -math.inf
for i in range(1, len(a)):
    memo[i] = max(memo[i-1] + a[i], a[i])
    if memo[i] > max_val:
        max_val = memo[i]
print(max_val)