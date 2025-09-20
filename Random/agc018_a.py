N, K = map(int, input().split())

A = list(map(int, input().split()))

if K in A:
    print('POSSIBLE')
    exit()

A.sort()

if A[-1] < K:
    print('IMPOSSIBLE')
    exit()

# Aの要素2つの差を集める
A_diffs = []
for i in range(1, N):
    A_diffs.append(A[i] - A[i - 1])

for diff in A_diffs:
    if K % diff == 0:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
