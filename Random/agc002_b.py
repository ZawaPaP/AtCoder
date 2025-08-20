N, M = map(int, input().split())

possibilities = [False] * (N + 1)
possibilities[1] = True

balls = [1] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())

    if possibilities[x]:
        possibilities[y] = True

    balls[x] -= 1
    balls[y] += 1
    if balls[x] == 0:
        possibilities[x] = False
print(sum(possibilities))
