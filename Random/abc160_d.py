from collections import deque

N, X, Y = map(int, input().split())

distance_counts = [0] * (N - 1)

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        dist = min(j - i, abs(X - i) + abs(Y - j) + 1)
        distance_counts[dist - 1] += 1

for i in range(N - 1):
    print(distance_counts[i])
