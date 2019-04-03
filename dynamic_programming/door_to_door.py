"""Suppose that you are a door-to-door salesman, selling the latest innovation in vacuum cleaners to
less-than-enthusiastic customers. Today, you are planning on selling to some of the n houses along a particular
street. You are a master salesman, so for each house, you have already worked out the amount ci of profit that
you will make from the person in house i if you talk to them. Unfortunately, you cannot sell to every house, since
if a person’s neighbour sees you selling to them, they will hide and not answer the door for you. Therefore, you
must select a subset of houses to sell to such that none of them are next to each other, and such that you make
the maximum amount of money.

1. Moving from left to right, we treat the inclusion or exclusion of  each door as a sub-problem P with a cost C 
associated with it. The goal is to maximise the overall cost, derived from the maximum of the previous door or 
addition of a new door added to the maximum cost of its previous doors, a set of P(excluding the immediate left).

2. A problem has overlapping sub-problems if the optimal sub-structure can be built up from these smaller sub-problems
and the calculation of associated costs of these sub-problems occur one or more times during a brute-force approach.

3. Base case is when there is 1 house - 50. OR 2 houses?

4. memo[i] = max(memo[i-1], houses[i] + max(memo[:i-1])

"""


TEST = [50, 10, 12, 65, 40, 95, 100, 12, 20, 30]

def solve_door_to_door(a):
    if len(a) <= 2:
        max_val = max(enumerate(a), key=lambda x: x[1])
        return max_val[1], [max_val[0]]
    memo = a[:2] + [0] * (len(a)-2)
    prev_max = (0, memo[0])
    for i in range(2, len(a)):
        choices = (a[i] + prev_max[1], memo[i-1])
        prev, memo[i] = max(enumerate(choices), key=lambda x: x[1])
        if memo[i-1] > prev_max[1]:
            prev_max = (i-1, memo[i-1])
    return memo[-1]


if __name__ == '__main__':
    result = solve_door_to_door(TEST)
    print(sum([x for i, x in enumerate(TEST) if i in (0, 3, 5, 7, 9)]))
    print(result)