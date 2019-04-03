import math


def coin_change_min_bottom_up(n, a):
    memo = [0] + [math.inf] * n
    for coin in a:
        for j in range(len(memo)):
            if j >= coin:
                memo[j] = min(memo[j], memo[j-coin] + 1)
    if memo[-1] == math.inf:
        return -1
    else:
        return memo[-1]


def coin_change_min_top_down(n, a):
    memo = [math.inf] * (n + 1)
    result = top_down_aux(n, a, memo)
    if result == math.inf:
        return -1
    else:
        return result


def top_down_aux(n, a, memo):
    if n == 0:
        return 0
    elif memo[n] != math.inf:
        return memo[n]
    for coin in a:
        if coin <= n:
            memo[n] = min(memo[n], top_down_aux(n - coin, a, memo) + 1)
    return memo[n]

if __name__ == '__main__':
    pass
    # print(coin_change_min_top_down(110, [1, 5, 10, 50]))
