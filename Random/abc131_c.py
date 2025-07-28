import math

A, B, C, D = map(int, input().split())

# A ~ Bの間にある Cの倍数の数は
c_multiples = B // C - (A - 1) // C
d_multiples = B // D - (A - 1) // D

# CとDの最小公倍数
lcm = C * D // math.gcd(C, D)

lcm_multiples = B // lcm - (A - 1) // lcm

print(B - A - c_multiples - d_multiples + lcm_multiples + 1)
