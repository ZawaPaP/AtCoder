H, W = map(int, input().split())

A = [list(map(int, input().split())) for i in range(H)]

C = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

ans = []

for i in range(H):
    s = []
    for j in range(W):
        if A[i][j] == 0:
            s.append(".")
        else:
            s.append(C[A[i][j] - 1])
    ans.append(s)


for i in range(H):
    print("".join(ans[i]))
