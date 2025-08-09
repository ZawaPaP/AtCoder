import math

MOD = 10 ** 9 + 7

N, M = map(int, input().split())

if abs(N - M) > 1:
    print(0)
    exit()

# N == M の時、犬と猿の場所は2通り
# N != M の時、犬と猿の場所は１通り

if N == M:
    print((math.factorial(N) % MOD * (math.factorial(M) % MOD) * 2) % MOD)
else:
    print((math.factorial(N) % MOD * math.factorial(M) % MOD) % MOD)
