N = int(input())

A = list(map(int, input().split()))

sunuke = A[0]
rascal = sum(A[1:])

ans = abs(sunuke - rascal)
for i in range(1, N - 1):
    sunuke += A[i]
    rascal -= A[i]
    ans = min(ans, abs(sunuke - rascal))

print(ans)
