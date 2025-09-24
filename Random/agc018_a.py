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
A_diffs = set()
for i in range(1, N):
    diff = A[i] - A[i - 1]
    A_diffs.add(diff)

for diff in A_diffs:
    if diff > 0 and K % diff == 0:  # diffが0でないことを確認
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')
