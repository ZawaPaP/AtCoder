N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = 0
for i in range(N):
    diff += abs(A[i] - B[i])

if (diff <= K and (K - diff) % 2 == 0):
    print("Yes")
else:
    print("No")
