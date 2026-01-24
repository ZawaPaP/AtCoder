N, Q = map(int, input().split())
A = list(map(int, input().split()))

sumA = [0] * (N + 1)
for i, v in enumerate(A):
    sumA[i + 1] = sumA[i] + v


ans = []
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        diff = A[x] - A[x - 1]
        A[x], A[x - 1] = A[x - 1], A[x]
        sumA[x] += diff

    if query[0] == 2:
        l, r = query[1], query[2]
        ans.append(sumA[r] - sumA[l - 1])

for a in ans:
    print(a)
