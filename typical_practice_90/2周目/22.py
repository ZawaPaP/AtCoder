A, B, C = map(int, input().split())


# ユークリッドの互除法
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# A, B, Cの最大公約数を見つける。
ab_gcd = gcd(A, B)
all_gcd = gcd(ab_gcd, C)

print(A // all_gcd + B // all_gcd + C // all_gcd - 3)
