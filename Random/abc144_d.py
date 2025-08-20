import math

a, b, x = map(int, input().split())

# S >= a * a * b / 2の時、水は台形
# そうでないとき水は三角形

rad = 0
if a * a * b / 2 >= x:
    rad = math.atan(a * b * b / (2 * x))
else:
    rad = math.atan((2 * b - 2 * x / a / a) / a)

print(rad / math.pi * 180)
