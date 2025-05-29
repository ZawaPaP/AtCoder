N, M = map(int, input().split())


min_l = 0
max_r = N

for _ in range(M):
    L, R = map(int, input().split())

    min_l = max(L, min_l)
    max_r = min(R, max_r)


print(max(0, max_r - min_l + 1))
