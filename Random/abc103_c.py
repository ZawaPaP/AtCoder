import math

N = int(input())

A = list(map(int, input().split()))

ans = 0
min_lcm = math.lcm(*A)

for a in A:
    ans += (min_lcm - 1) % a

print(ans)
