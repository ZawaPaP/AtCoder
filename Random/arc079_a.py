N, M = map(int, input().split())

roads = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

road_from_1 = roads[1]
road_from_N = set(roads[N])

for road in road_from_1:
    if road in road_from_N:
        print("POSSIBLE")
        exit()

print("IMPOSSIBLE")
