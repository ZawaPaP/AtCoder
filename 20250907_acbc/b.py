H, W = map(int, input().split())

Grid = [list(input()) for _ in range(H)]

next = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = "Yes"
for i in range(H):
    for j in range(W):
        if Grid[i][j] == '.':
            continue
        black_count = 0
        for di, dj in next:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and Grid[ni][nj] == '#':
                black_count += 1
        if black_count != 2 and black_count != 4:
            ans = "No"
            print(ans)
            exit()

print(ans)
