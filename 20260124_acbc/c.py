import math

N, M = map(int, input().split())

relation = {}

for _ in range(M):
    a, b = map(int, input().split())
    relation[a] = relation.get(a, 0) + 1
    relation[b] = relation.get(b, 0) + 1

ans = []
for i in range(1, N + 1):
    remain = N - 1 - relation.get(i, 0)
    ans.append(math.comb(remain, 3))

print(*ans)
