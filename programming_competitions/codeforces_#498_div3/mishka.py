n = int(input())
a = list(map(int, input().split()))
for k in a:
    if k % 2 == 0:
        print(k-1, end=" ")
    else:
        print(k, end=" ")
