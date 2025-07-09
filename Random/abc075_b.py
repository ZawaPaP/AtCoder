H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]


def get_surround_mine_count(S, x, y):
    if S[x][y] != ".":
        return 0

    count = 0
    for k in range(x - 1, x + 2):
        for l in range(y - 1, y + 2):
            if k < 0 or l < 0 or k >= H or l >= W:
                continue
            if S[k][l] == "#":
                count += 1
    return count


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        else:
            S[i][j] = get_surround_mine_count(S, i, j)

for s in S:
    print(*s, sep="")
