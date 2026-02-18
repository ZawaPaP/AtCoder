L, R = map(int, input().split())
MOD = 10**9 + 7
# ex.
# 桁数ごとに求めていけば良い

l_len = len(str(L))
r_len = len(str(R))
# L と Rの桁数が同じであれば単に等差数列 * 桁数で求められる
if l_len == r_len:
    ans = (L + R) * (R - L + 1) // 2
    ans %= MOD
    print((ans * l_len) % MOD)
    exit()

ans = 0
# 異なる場合、Lの桁の和を計算
l_keta_max = 10**l_len - 1
ans += (l_keta_max + L) * (l_keta_max - L + 1) // 2 * l_len
ans %= MOD

# ある桁の等差数列の和 * 桁数
keta = l_len + 1
a = 10**l_len
while keta < r_len:
    b = 10 * a - 1
    ans += (a + b) * (10 * a - a) // 2 * keta
    ans %= MOD
    keta += 1
    a *= 10

# Rの桁の和を計算
r_keta_min = 10 ** (r_len - 1)
ans += (r_keta_min + R) * (R - r_keta_min + 1) // 2 * r_len
ans %= MOD

print(ans)
