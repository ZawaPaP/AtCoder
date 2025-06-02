N = int(input())

P = list(map(int, input().split()))

ans = 0
min_num = P[0]
for p in P:
    if min_num >= p:
        ans += 1
        min_num = p

print(ans)
