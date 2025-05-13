H, W = map(int, input().split())

A = []
B = []

for _ in range(H):
    temp = list(map(int, input().split()))

    A.append(temp)

for _ in range(H):
    temp = list(map(int, input().split()))

    B.append(temp)

# A[i][j]、B[i][j] の差についてdiff Diff[i][j]をとる

Diff = [[0] * W for _ in range(H)]


for i in range(H):
    for j in range(W):
        Diff[i][j] = A[i][j] - B[i][j]

count = 0

for i in range(H - 1):
    for j in range(W - 1):
        if Diff[i][j] == 0:
            continue

        # Diffが0ではない場合、0になるように
        # Diff[i][j], Diff[i + 1][j], Diff[i][j + 1], Diff[i + 1][j + 1]
        # に同じ数を加える
        d = Diff[i][j]  # 一時変数に保存
        Diff[i][j] -= d
        Diff[i + 1][j] -= d
        Diff[i][j + 1] -= d
        Diff[i + 1][j + 1] -= d
        count += abs(d)

for i in range(H):
    for j in range(W):
        if Diff[i][j] != 0:
            print("No")
            exit()

print("Yes")
print(count)
