N, K = map(int, input().split())

A = list(map(int, input().split()))

ans = A[0]

for i in range(1, N):
    if len(str(ans)) > K:
        ans = 1
    ans *= A[i]

if len(str(ans)) > K:
    ans = 1
print(ans)
