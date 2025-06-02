N, M = map(int, input().split())

favorites = {}

for _ in range(N):
    lst = list(map(int, input().split()))

    for i in range(1, len(lst)):
        if lst[i] in favorites:
            favorites[lst[i]] += 1
        else:
            favorites[lst[i]] = 1

ans = 0
for values in favorites.values():
    if values == N:
        ans += 1


print(ans)
