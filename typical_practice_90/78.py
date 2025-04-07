N, M = map(int, input().split())

d = {}

for _ in range(M):
    a, b = map(int, input().split())
    if a in d:
        d[a].append(b)
    else:
        d[a] = [b]
    if b in d:
        d[b].append(a)
    else:
        d[b] = [a]

ans = 0
for key, value in d.items():
    count = 0
    for v in value:
        if key > v:
            count += 1
    if count == 1:
        ans += 1

print(ans)
