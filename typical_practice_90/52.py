N = int(input())

MOD = 10**9 + 7

A = []

for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)


ans = 1

for i in range(N):
    ans *= sum(A[i])
    ans %= MOD

print(ans)
