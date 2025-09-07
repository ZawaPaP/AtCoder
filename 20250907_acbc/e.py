import sys
import random

input = sys.stdin.buffer.readline

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
over_mid = N // 2 + 1


def line(p1, p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0] * p1[1] - p1[0] * p2[1]
    return a, b, c


def on_line(p, a, b, c):
    return a * p[0] + b * p[1] + c == 0


T = 80  # 試行回数
for _ in range(T):
    i, j = random.sample(range(N), 2)
    a, b, c = line(points[i], points[j])
    cnt = sum(on_line(p, a, b, c) for p in points)
    if cnt >= over_mid:
        print("Yes")
        print(a, b, c)
        sys.exit(0)

print("No")
