# https://atcoder.jp/contests/abc106/tasks/abc106_b

N = int(input())


def count_divisors(n):
    i = 1
    divisors = []
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
        i += 1
    return len(divisors)


ans = 0
for i in range(N + 1):
    if i % 2 == 0:
        continue
    if count_divisors(i) == 8:
        ans += 1
print(ans)
