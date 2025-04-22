N, L = map(int, input().split())

MOD = 10**9 + 7

Steps = [0] * (N + 1)
Steps[0] = 1

for i in range(1, N + 1):
    Steps[i] += Steps[i - 1]

    if i - L >= 0:
        Steps[i] += Steps[i - L]

print(Steps[N] % MOD)
