N, M = map(int, input().split())

MOD = 10 ** 9 + 7

stairs = [0] * (N + 1)
broken = [False] * (N + 1)

for _ in range(M):
    a = int(input())
    broken[a] = True

stairs[0] = 1

for i in range(1, N + 1):
    if broken[i]:
        stairs[i] = 0
        continue
    if i == 1:
        stairs[i] = 1
    else:
        stairs[i] = (stairs[i - 1] + stairs[i - 2]) % MOD

print(stairs[N])
