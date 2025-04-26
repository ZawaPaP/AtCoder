L, R = map(int, input().split())

MOD = 10**9 + 7


def get_ketasu(num):
    return len(str(num))


def make_nines(n):
    return int("9" * n)


def sigma(l, r):
    sum = 0
    if (l + r) % 2 == 0:
        sum = (l + r) * (r - l) // 2 + (l + r) // 2
    else:
        sum = (l + r) * ((r - l) // 2 + 1)
    return sum


L_keta = get_ketasu(L)
R_keta = get_ketasu(R)

ans = 0

if L_keta == R_keta:
    ans = sigma(L, R) % MOD * L_keta
    print(ans % MOD)
    exit()

ans += sigma(10 ** (R_keta - 1), R) % MOD * R_keta
temp = R_keta - 1

while L_keta < temp:
    ans += sigma(10 ** (temp - 1), make_nines(temp)) % MOD * temp
    temp -= 1

ans += sigma(L, make_nines(L_keta)) % MOD * L_keta

print(ans % MOD)
