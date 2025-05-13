N = int(input())

A = list(map(int, input().split()))

sum_A = sum(A)

ans = 0

for i in range(N - 1):
    ans += A[i] * sum_A
    ans -= A[i] * A[i]
    sum_A -= A[i]

print(ans)
