def binomial_coefficients(n, k):
    if n < k:
        return 0
    if k == 0 or n == k:
        return 1
    return binomial_coefficients(n-1, k-1) + binomial_coefficients(n-1, k)


def binomial_coefficients_dp(n, k):
    memo = [[0] * (k+1) for _ in range(n+1)]
    memo[0] = [0] + [1 for _ in range(1, k+1)]
    for j in range(1, len(memo)):
        memo[j][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i >= j:
                memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
    return memo[-1][-1]


print(binomial_coefficients(50, 3))
print(binomial_coefficients_dp(50, 3))
