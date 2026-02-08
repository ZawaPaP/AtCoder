from collections import Counter

N = map(int, input().split())

A = list(map(int, input().split()))

sum_A = sum(A)

# Lの取りうる値は maxA以上の sum_Aの約数


def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


divisors = make_divisors(sum_A)

ans_candidates = []
for d in divisors:
    if d >= max(A):
        ans_candidates.append(d)

# candidatesに対して、それぞれ条件を満たすか線形操作
sorted_A = sorted(A, reverse=True)
map_A = Counter(sorted_A)

ans = []
for L in ans_candidates:
    temp_mp = map_A.copy()
    isPossible = True

    for n in sorted_A:
        if temp_mp[n] == 0:
            continue

        temp_mp[n] -= 1

        if n == L:
            continue
        else:
            remain = L - n
            if temp_mp[remain] > 0:
                temp_mp[remain] -= 1
            else:
                isPossible = False
                break
    if isPossible:
        ans.append(L)

print(*ans)
