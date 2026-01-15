H, W = map(int, input().split())

Grid = [list(map(int, input().split())) for _ in range(H)]

each_row_sums = []
each_col_sums = [0 for _ in range(W)]

for row in Grid:
    each_row_sums.append(sum(row))

for row in Grid:
    for i, n in enumerate(row):
        each_col_sums[i] += n

ans = [row[:] for row in Grid]
for r in range(H):
    for c in range(W):
        temp = ans[r][c]
        ans[r][c] = each_row_sums[r] + each_col_sums[c] - temp

for a in ans:
    print(*a)
