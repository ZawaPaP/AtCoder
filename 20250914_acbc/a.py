X, C = map(int, input().split())

ans = 0
for i in range(0, X // 1000 + 1):
    cost = i * 1000 * (1 + C / 1000)
    if cost <= X:
        ans = i * 1000

print(ans)
