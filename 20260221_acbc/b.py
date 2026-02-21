N, M = map(int, input().split())

Stock = [True] * M

drink = []
for _ in range(N):
    L = int(input())
    X = list(map(int, input().split()))

    delivered = False
    for x in X:
        if Stock[x - 1]:
            Stock[x - 1] = False
            drink.append(x)
            delivered = True
            break
    if not delivered:
        drink.append(0)

for d in drink:
    print(d)
