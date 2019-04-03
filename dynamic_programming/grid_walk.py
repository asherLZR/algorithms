# 7 7
# -1 -1 0 0 -1 -1 0
# -1 -1 0 0 0 0 0
# 0 0 0 0 0 -1 0
# 0 0 0 0 -1 0 0
# 0 -1 0 0 0 0 0
# 0 -1 -1 0 0 -1 -1
# 0 0 0 0 0 -1 0

import copy


def solve_grid_walk_bfs(grid):
    start = (n-1, 0)
    possible = [(-1, 0), (0, 1)]
    q = [start]
    while q:
        current = q.pop(0)
        grid[current[0]][current[1]] += 1
        for direction in possible:
            pos = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= pos[0] <= (n - 1) and 0 <= pos[1] <= (m - 1) and grid[pos[0]][pos[1]] != -1:
                q.append(pos)
    for r in grid:
        print(r)
    print(grid[0][m - 1])


def solve_grid_walk_dp(grid):
    grid[n-1][0] = 1
    for i in range(n-1, -1, -1):
        for j in range(m):
            if grid[i][j] == -1:
                grid[i][j] = 0
            else:
                if i == n-1 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i][j-1] + grid[i+1][j]
    for r in grid:
        print(r)
    print(grid[0][m-1])


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    solve_grid_walk_bfs(copy.deepcopy(a))
    print()
    solve_grid_walk_dp(copy.deepcopy(a))


