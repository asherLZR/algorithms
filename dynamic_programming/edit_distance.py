def edit_distance(first, second):
    memo = [[0] * (len(first)+1) for _ in range(len(second)+1)]
    for i in range(len(first)+1):
        memo[0][i] = i
    for j in range(len(second)+1):
        memo[j][0] = j
    for i in range(1, len(second)+1):
        for j in range(1, len(first)+1):
            if second[i-1] != first[j-1]:
                memo[i][j] = min(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]) + 1
            else:
                memo[i][j] = min(memo[i-1][j]+1, memo[i][j-1]+1, memo[i-1][j-1])
    return memo[-1][-1]

# https://www.hackerrank.com/contests/cse-830-homework-3/challenges/edit-distance/submissions/code/1307378580
