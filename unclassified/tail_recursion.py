# -- Tail Recursion --
# Where the result of the recursive call is the result of the function/
# Nothing is performed on the "way back". Closest to iteration - can be
# transformed without "storing". Useful for compiler optimisation.

# Python does not optimise for tail recursion because it prevents a
# proper traceback.


def sum_of_digits(x):
    if x < 10:
        return x
    else:
        return x % 10 + sum_of_digits(x // 10)


def sum_of_digits_tail(x, running_sum=0):
    if x < 10:
        return running_sum + x
    else:
        return sum_of_digits_tail(x // 10, running_sum + (x % 10))


def sum_of_digits_iterative(x, running_sum=0):
    while True:
        if x < 10:
            return running_sum + x
        else:
            x, running_sum = x//10, running_sum + (x % 10)


print(sum_of_digits(35))
print(sum_of_digits_tail(35))
print(sum_of_digits_iterative(35))
