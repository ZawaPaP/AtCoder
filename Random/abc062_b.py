H, W = map(int, input().split())
A = [input() for _ in range(H)]


ans = [["#"] * (W + 2) for _ in range(H + 2)]

for i in range(H + 2):
    for j in range(W + 2):
        if i > 0 and j > 0 and i < H + 1 and j < W + 1:
            ans[i][j] = A[i - 1][j - 1]

for row in ans:
    print("".join(row))
