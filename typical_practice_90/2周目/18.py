import math

T = int(input())
L, X, Y = map(int, input().split())

Q = int(input())
degs = []

for _ in range(Q):
    E = int(input())

    E %= T
    rad = math.radians(360 * E / T)

    # 観覧車のy
    cart_y = - math.sin(rad) * L / 2
    # 観覧車のz
    cart_z = L / 2 - math.cos(rad) * L / 2

    # 観覧車から像への距離
    length = math.sqrt((Y - cart_y)**2 + X**2)

    # 俯角
    degs.append(math.degrees(math.atan2(cart_z, length)))

for d in degs:
    print(d)
