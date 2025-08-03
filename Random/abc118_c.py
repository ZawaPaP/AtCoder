import math

N = int(input())

A = list(map(int, input().split()))

ans = math.gcd(*A)

print(ans)
