N, L = map(int, input().split())
MOD = 10**9 + 7

count = [0] * (N + 1)

count[0] = 1

for i in range(1, N + 1):
    if i >= L:
        count[i] += count[i - L]
    count[i] += count[i - 1]

    count[i] %= MOD

print(count[N])
