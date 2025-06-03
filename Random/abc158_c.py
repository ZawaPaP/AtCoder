import math

A, B = map(int, input().split())

net_price = max(B // 0.1, A // 0.08) + 1

if math.floor(net_price * 0.1) == B and math.floor(net_price * 0.08) == A:
    print(int(net_price))
else:
    print(-1)
