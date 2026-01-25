import math

A, B = map(int, input().split())

MAX = 10**18


def get_lcm(a, b):
    return a * b // math.gcd(a, b)


lcm = get_lcm(A, B)

if lcm > MAX:
    print("Large")
else:
    print(lcm)
