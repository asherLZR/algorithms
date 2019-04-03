# given a list of positive integers, maximise the sum of a set of integers that are divisible
# by one chosen number

if __name__ == "__main__":
    n = int(input())
    a = sorted(list(map(int, input().split())))
    memo = [0] * (max(a) + 1)
    j = 0
    for i in range(1, len(memo)):
        memo[i] = memo[i-1]
        if j == len(a):
            break
        while j < len(a) and a[j] <= i:
            memo[i] += 1
            j += 1
    mp = 0
    for v in a:
        cs = 0
        i = 2
        while (v * i - 1) < len(memo):
            prv = memo[v * (i-1)-1]
            nxt = memo[v * i-1]
            cs += (i-1) * (nxt-prv)
            i += 1
        if len(memo)-1 > (v * (i-1)-1):
            prv = memo[v * (i-1) - 1]
            nxt = memo[len(memo)-1]
            cs += (i-1) * (nxt-prv)
        cs *= v
        mp = max(cs, mp)
    print(mp)
