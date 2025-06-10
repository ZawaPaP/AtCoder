N, M = map(int, input().split())

stocks = []

for _ in range(N):
    A, B = map(int, input().split())
    stocks.append((A, B))

stocks.sort()

total = 0
price = 0

for stock in stocks:
    if total >= M:
        break
    if total + stock[1] <= M:
        total += stock[1]
        price += stock[0] * stock[1]

    else:
        nokori = M - total
        price += stock[0] * nokori
        break

print(price)
