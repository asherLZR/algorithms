def fib(n):
    """
    Complexity: 2^n
    """
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def fib_aux(n, before_last, last):
    if n == 0:
        return before_last
    else:
        return fib_aux(n-1, last, before_last+last)


def fib_memo(n):
    memo = [None] * (n + 1)
    if n == 0:
        return 0
    if n < 2:
        return 1
    if memo[n] is not None:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]


def fib_bottom_up(n):
    memo = [0, 0]
    for i in range(n+1):
        if i == 0:
            memo[0] = 0
        elif i == 1:
            memo[1] = 1
        else:
            memo[0], memo[1] = memo[1], memo[0] + memo[1]
    return memo[1]

def fib_matrix(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    if n % 2 == 0:
        n /= 2
        return fib_matrix(n) * (2 * fib_matrix(n+1) - fib_matrix(n))
    else:
        n = (n-1)/2
        return fib_matrix(n+1)**2 + fib_matrix(n)**2

val = 50
# print(fib_memo(val))
# print(fib_bottom_up(val))
# print(fib_aux(val, 0, 1))
print(fib(val))
print(fib_matrix(val))
# F(k)[2F(k +1)−F(k)]


# def factorial(n):
#     if n <= 1:
#         return 1
#     return factorial(n-1)*n
#
#
# def sumCubes(total, power, num):
#     value = total - num**power
#     if value < 0:
#         return 0
#     elif value == 0:
#         return 1
#     else:
#         return sumCubes(value, power, num+1) + sumCubes(total, power, num+1)
#
# print(sumCubes(100, 3, 1))

