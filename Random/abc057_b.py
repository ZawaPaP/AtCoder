N, M = map(int, input().split())

students = []

for _ in range(N):
    a, b = map(int, input().split())
    students.append([a, b])

checks = []

for _ in range(M):
    c, d = map(int, input().split())
    checks.append([c, d])

gather_points = []

for student in students:
    closest_index = -1
    min_distance = float("INF")
    for i, check in enumerate(checks):
        dist = abs(student[0] - check[0]) + abs(student[1] - check[1])
        if dist < min_distance:
            min_distance = min(min_distance, dist)
            closest_index = i
    gather_points.append(closest_index)

for point in gather_points:
    print(point + 1)
