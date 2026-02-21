# https://atcoder.jp/contests/abc095/tasks/arc096_a
A, B, C, X, Y = map(int, input().split())

price = 0
# A + B > 2Cの時、共通枚数分Cを買う
if A + B > 2 * C:
    common = min(X, Y)
    price += common * 2 * C
    X -= common
    Y -= common

# A > 2*C の時、Aピザのために常にCを買う
if A > 2 * C and X > 0:
    price += X * 2 * C
    X -= X
    Y -= X
if B > 2 * C and Y > 0:
    price += Y * 2 * C
    X -= Y
    Y -= Y

# AをX分買う
if X > 0:
    price += A * X
if Y > 0:
    price += B * Y

print(price)
