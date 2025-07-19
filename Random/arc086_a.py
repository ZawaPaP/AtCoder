N, K = map(int, input().split())

A = list(map(int, input().split()))

d = {}

for a in A:
    d[a] = d.get(a, 0) + 1

d = sorted(d.items(), key=lambda x: x[1])

if len(d) <= K:
    print(0)
else:
    ans = 0
    for i in d[:-K]:
        ans += i[1]
    print(ans)
