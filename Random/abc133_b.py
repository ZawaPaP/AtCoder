import math

N, D = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        double_dist = 0
        for k in range(D):
            double_dist += (X[i][k] - X[j][k]) ** 2

        dist = math.sqrt(double_dist)
        if dist == int(dist):
            ans += 1

print(ans)
