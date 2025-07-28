import itertools

N, K, X = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

strings = []

for v in itertools.product(S, repeat=K):
    strings.append("".join(v))

print(sorted(strings)[X - 1])
