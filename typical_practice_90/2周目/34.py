N, K = map(int, input().split())
A = list(map(int, input().split()))
l, r = 0, 0
counts = {}
max_len = 0

for r in range(N):
    counts[A[r]] = counts.get(A[r], 0) + 1
    while len(counts) > K:
        counts[A[l]] -= 1
        if counts[A[l]] == 0:
            del counts[A[l]]
        l += 1
    max_len = max(max_len, r - l + 1)

print(max_len)
