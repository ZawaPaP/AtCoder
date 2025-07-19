N, K = map(int, input().split())

P = list(map(int, input().split()))

Kitaichis = []

for p in P:
    if p % 2 == 1:
        Kitaichis.append(p // 2 + 1)
    else:
        Kitaichis.append((p + 1) / 2)

ans = sum(Kitaichis[:K])
temp = ans
for i in range(K, N):
    temp += Kitaichis[i] - Kitaichis[i - K]
    ans = max(ans, temp)

print(ans)
