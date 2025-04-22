import itertools
import math


# 点xの座標を求める
def get_coordinate(p):
    rad = math.radians(360 / N * p)
    x = math.sin(rad)
    y = math.cos(rad)
    return [x, y]


# 2点間p1[x, y], p2[x, y]傾きを求める
def calc_rad(p1, p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    return round(a / (-b), 8)


N, M = map(int, input().split())

katamuki_dic = {}

for _ in range(M):
    a, b = map(int, input().split())
    a_coordinate = get_coordinate(a)
    b_coordinate = get_coordinate(b)
    katamuki = calc_rad(a_coordinate, b_coordinate)

    if katamuki in katamuki_dic:
        katamuki_dic[katamuki] += 1
    else:
        katamuki_dic[katamuki] = 1


key_list = list(katamuki_dic.keys())
combinations = list(itertools.combinations(key_list, 2))

ans = 0
for combination in combinations:
    ans += katamuki_dic[combination[0]] * katamuki_dic[combination[1]]

print(ans)
