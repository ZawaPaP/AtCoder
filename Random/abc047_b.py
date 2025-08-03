W, H, N = map(int, input().split())

x_min = 0
x_max = W
y_min = 0
y_max = H

for _ in range(N):
    x, y, a = map(int, input().split())

    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    elif a == 4:
        y_max = min(y_max, y)

print(max(0, x_max - x_min) * max(0, y_max - y_min))
