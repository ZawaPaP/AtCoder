import math

T = int(input())
L, X, Y = map(int, input().split())

Q = int(input())

for _ in range(Q):
    E = int(input())
    E %= T
    # 角度を計算（0-360度）
    angle = (E / T) * 360
    radian = math.radians(angle)

    x = X
    y = -L / 2 * math.sin(radian)
    z = L / 2 - (L / 2 * math.cos(radian))

    # 像までの平面距離
    distance_to_chokudai = math.sqrt(x**2 + (Y - y) ** 2)

    # tangentを使って俯角を求める。
    print(math.degrees(math.atan2(z, distance_to_chokudai)))
