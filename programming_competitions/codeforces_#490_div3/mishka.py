n, k = list(map(int, input().split(" ")))
a_list = list(map(int, input().split(" ")))
i, j = 0, len(a_list)-1
count = 0
while i <= j:
    if a_list[i] <= k:
        count += 1
        i += 1
    elif a_list[j] <= k:
        count += 1
        j -= 1
    else:
        break
print(count)
