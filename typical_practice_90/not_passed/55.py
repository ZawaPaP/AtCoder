N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

from itertools import combinations

ans = 0
for a, b, c, d, e in combinations(A, 5):
    if a * b % P * c % P * d % P * e % P == Q:
        ans += 1

print(ans)
