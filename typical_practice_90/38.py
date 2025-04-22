A, B = map(int, input().split())

MAX_ANS = 1000000000000000000


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


ans = A // gcd(A, B) * B

if ans > MAX_ANS:
    print("Large")
else:
    print(ans)
