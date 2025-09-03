import math

A, B = map(int, input().split())

# Aの素数を列挙
a_primes = set()

for i in range(2, int(A ** 0.5) + 1):
    while A % i == 0:
        A //= i
        a_primes.add(i)
if A > 1:
    a_primes.add(A)


common_primes = []

for i in a_primes:
    if B % i == 0:
        common_primes.append(i)

# 1を追加
print(len(common_primes) + 1)
