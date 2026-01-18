N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_ops = 0
for i in range(N):
    min_ops += abs(A[i] - B[i])

if K >= min_ops and (K - min_ops) % 2 == 0:
    print("Yes")
    exit()

print("No")
