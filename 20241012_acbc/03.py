N = int(input())

matrix = []
for _ in range(N):
    row = list(input())
    matrix.append(row)

# i = 1 だけをまず考える

# 1以上 N + 1 - 1 以下の整数 x,y について
# (y,N+1−x) の色をマス (x,y)の色とする

new_matrix = [row[:] for row in matrix]


for i in range(1, N // 2 + 1):
    for x in range(i, N + 2 - i):
        for y in range(i, N + 2 - i):
            new_matrix[y - 1][N + 1 - x - 1] = matrix[x - 1][y - 1]
    matrix = [row[:] for row in new_matrix]

print("\n".join(["".join(row) for row in new_matrix]))


# 問題文が複雑だったが、実際には、マス (x,y) について、(y,N+1−x) の色をマス (x,y) の色とするという操作を
# 繰り返すと、90度回転していくため、4回繰り返すと元のマスと同じになることがわかる。
