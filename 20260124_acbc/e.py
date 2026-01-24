import math

N, Q = map(int, input().split())

degrees = []
for i in range(N):
    x, y = map(int, input().split())
    radian = math.atan2(y, x)
    degrees.append((radian, i + 1))

sorted_degrees = sorted(degrees, key=lambda x: x[0], reverse=True)

# 元の番号からソート後の位置を弾けるようにする
rank = [0] * (N + 1)
for i in range(N):
    _, original_id = sorted_degrees[i]
    rank[original_id] = i + 1

# 同じ格の場合のため、L, R を記録
L = [0] * (N + 1)
R = [0] * (N + 1)

i = 0
while i < N:
    j = i
    while j < N and sorted_degrees[j][0] == sorted_degrees[i][0]:
        j += 1
    # [i + 1, j]は全て同じ角度
    start_pos = i + 1
    end_pos = j
    for k in range(start_pos, end_pos + 1):
        L[k] = start_pos
        R[k] = end_pos
    i = j

ans = []
for _ in range(Q):
    a, b = map(int, input().split())

    # 点の番号から、ソート後の位置を取得
    a_pos = rank[a]
    b_pos = rank[b]

    la = L[a_pos]
    rb = R[b_pos]

    if la <= rb:
        ans.append(rb - la + 1)
    else:
        ans.append(N - la + 1 + rb)

for an in ans:
    print(an)
