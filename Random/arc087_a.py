N = int(input())

A = list(map(int, input().split()))

counts = {}

for a in A:
    counts[a] = counts.get(a, 0) + 1

ans = 0
for k, v in counts.items():
    if k > v:
        ans += v
    elif k < v:
        ans += v - k

print(ans)
