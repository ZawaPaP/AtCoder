import math

N, X = map(int, input().split())

x = list(map(int, input().split()))

x.append(X)

x.sort()

diff = []

for i in range(len(x) - 1):
    diff.append(x[i + 1] - x[i])

for i in range(len(diff)):
    if i == 0:
        gcd = diff[i]
    else:
        gcd = math.gcd(gcd, diff[i])

print(gcd)
