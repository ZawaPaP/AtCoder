import math

MOD = 10 ** 9 + 7

N = int(input())

# 1 ~ N までを素因数分解し、各素因数の数を数える
# prime_factors[i] は 素因数分解した時のiの指数
prime_factors = [0] * (N + 1)


for i in range(1, N + 1):
    # iを素因数分解し, prime_factors[j] にjの指数を加算
    while i % 2 == 0:
        prime_factors[2] += 1
        i //= 2
    f = 3
    while f * f <= i:
        if i % f == 0:
            prime_factors[f] += 1
            i //= f
        else:
            f += 2
    if i > 1:
        prime_factors[i] += 1


ans = 1
for i in prime_factors:
    ans *= i + 1
    ans %= MOD

print(ans)
