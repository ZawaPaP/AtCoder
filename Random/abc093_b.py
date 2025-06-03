A, B, K = map(int, input().split())

ans = set()

for i in range(A, B + 1):
    if i <= A + K - 1 or i >= B + 1 - K:
        ans.add(i)

for a in ans:
    print(a)
