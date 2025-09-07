from collections import deque

sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

ans = ""

moves = {
    'U': (0, 1),
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
}

# 最初の往復は最短距離
ans += 'U' * (ty - sy)
ans += 'R' * (tx - sx)
ans += 'D' * (ty - sy)
ans += 'L' * (tx - sx)

# 2回目の往復は最短よりも1つ外側を通る
ans += 'L'
ans += 'U' * (ty - sy + 1)
ans += 'R' * (tx - sx + 1)
ans += 'D'

ans += 'R'
ans += 'D' * (ty - sy + 1)
ans += 'L' * (tx - sx + 1)
ans += 'U'

print(ans)
