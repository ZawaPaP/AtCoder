N, M = map(int, input().split())

roads = {}

for i in range(1, N + 1):
    roads[i] = 0

for _ in range(M):
    a, b = map(int, input().split())

    if a in roads:
        roads[a] += 1

    if b in roads:
        roads[b] += 1


for value in roads.values():
    print(value)
