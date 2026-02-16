import math

N = int(input())

# 素因数分解が 2の何乗か、という問題


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2

    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


print(math.ceil(math.log2(len(prime_factorize(N)))))
