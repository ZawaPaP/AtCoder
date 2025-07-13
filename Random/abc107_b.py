H, W = map(int, input().split())
Grid = [list(input()) for _ in range(H)]
for i in range(H - 1, -1, -1):
    if "#" not in Grid[i]:
        del Grid[i]

for i in range(W - 1, -1, -1):
    column = [row[i] for row in Grid]
    if "#" not in column:
        for line in Grid:
            del line[i]


for row in Grid:
    print("".join(row))
