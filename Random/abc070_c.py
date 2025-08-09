import math


N = int(input())

T = [int(input()) for _ in range(N)]

ans = math.lcm(*T)

print(ans)
