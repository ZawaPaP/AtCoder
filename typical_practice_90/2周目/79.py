H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# Aのgridを左上から1つづつ見ていき、Bとの差分を計算していく

cnt = 0
for r in range(H - 1):
    for c in range(W - 1):
        if A[r][c] == B[r][c]:
            continue

        diff = B[r][c] - A[r][c]

        A[r][c] += diff
        A[r + 1][c] += diff
        A[r][c + 1] += diff
        A[r + 1][c + 1] += diff
        cnt += abs(diff)

if A == B:
    print("Yes")
    print(cnt)
else:
    print("No")
