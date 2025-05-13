N = int(input())

coordinates = []

for _ in range(N):
    coordinate = list(map(int, input().split()))
    coordinates.append(coordinate)

# 0 - 1000 の長方形のベースを用意
base = [[0 for _ in range(1001)] for _ in range(1001)]

for coordinate in coordinates:
    lx, ly, rx, ry = coordinate
    base[lx][ly] += 1
    base[lx][ry] -= 1
    base[rx][ly] -= 1
    base[rx][ry] += 1

# 横方向の累積和
for i in range(1001):
    for j in range(1, 1001):
        base[i][j] += base[i][j - 1]

# 縦方向の累積和
for i in range(1, 1001):
    for j in range(1001):
        base[i][j] += base[i - 1][j]

# 面積ごとのカウントを集計
answer = [0] * (N + 1)
for i in range(1001):
    for j in range(1001):
        if base[i][j] > 0:
            answer[base[i][j]] += 1

for k in range(1, N + 1):
    print(answer[k])
