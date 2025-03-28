N = int(input())

A = list(map(int, input().split()))

map = {}

ans = float("inf")

for i in range(N):
    if A[i] not in map:
        map[A[i]] = i
    else:
        ans = min(ans, i - map[A[i]] + 1)
        map[A[i]] = i

print(ans if ans != float("inf") else -1)
