N, M = map(int, input().split())

exchange_rates = []

for _ in range(M):
    a, b = map(int, input().split())
    d = a - b
    exchange_rates.append((a, b, d))

exchange_rates.sort(key=lambda x: x[2])

ans = 0
for exchange_rate in exchange_rates:
    a, b, d = exchange_rate

    if a > N:
        continue

    change_count = (N - a) // d + 1
    ans += change_count
    N -= change_count * d

print(ans)
