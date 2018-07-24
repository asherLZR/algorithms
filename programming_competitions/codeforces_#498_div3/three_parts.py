n = int(input())
a = list(map(int, input().split()))

i, j = 0, n-1
max_sum = 0
l_sum, r_sum = 0, 0
while i <= j:
    if l_sum < r_sum:
        l_sum += a[i]
        i += 1
    else:
        r_sum += a[j]
        j -= 1
    if l_sum == r_sum:
        max_sum = l_sum
print(max_sum)
