N = int(input())
SIZE = 1001
grid = [[0] * SIZE for _ in range(SIZE)]

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())

    grid[ry][lx] -= 1
    grid[ry][rx] += 1
    grid[ly][lx] += 1
    grid[ly][rx] -= 1

for y in range(SIZE):
    for x in range(1, SIZE):
        grid[y][x] += grid[y][x-1]

for x in range(SIZE):
    for y in range(1, SIZE):
        grid[y][x] += grid[y-1][x]

ans = [0] * (N + 1)
for y in range(SIZE):
    for x in range(SIZE):
        val = grid[y][x]
        if val > 0:
            ans[val] += 1

for i in range(1, N + 1):
    print(ans[i])
