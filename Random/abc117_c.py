N, M = map(int, input().split())

X = list(map(int, input().split()))

if N >= M:
    print(0)
    exit()

X.sort()

diffs = [X[i + 1] - X[i] for i in range(M - 1)]

diffs.sort()

print(sum(diffs[: M - N]))
