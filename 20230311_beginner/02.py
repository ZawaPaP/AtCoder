N = int(input())

A = list(map(int, input().split()))

S = set()

for i in range(N):
    if i + 1 in S:
        continue
    else:
        S.add(A[i])

K = N - len(S)

ans = []
for i in range(1, N + 1):
    if i in S:
        continue
    else:
        ans.append(i)

print(K)
print(*ans)