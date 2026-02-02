import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

D = []
base_diff = 0
for i in range(N - 1):
    diff = A[i + 1] - A[i]
    D.append(diff)
    base_diff += abs(diff)

for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1

    if L > 0:
        target_idx = L - 1
        base_diff -= abs(D[target_idx])
        D[target_idx] += V
        base_diff += abs(D[target_idx])
    if R < N - 1:
        target_idx = R
        base_diff -= abs(D[target_idx])
        D[target_idx] -= V
        base_diff += abs(D[target_idx])
    print(base_diff)
