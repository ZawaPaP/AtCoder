x, y = map(int, input().split())


if x == y:
    print(0)
    exit()


if abs(y) >= abs(x):
    if x >= 0 and y >= 0:
        print(y - x)
    elif x < 0 and y < 0:
        print(abs(y) - abs(x) + 2)
    elif x >= 0 and y < 0:
        print(abs(y) - abs(x) + 1)
    elif x < 0 and y >= 0:
        print(abs(y) - abs(x) + 1)
else:
    if x >= 0 and y >= 0:
        print(min(x + y + 1, abs(x) - abs(y) + 2))
    elif x < 0 and y < 0:
        print(abs(x) - abs(y))
    elif x >= 0 and y < 0:
        print(abs(x) - abs(y) + 1)
    elif x < 0 and y >= 0:
        print(min(abs(x) + abs(y), abs(x) - abs(y) + 1))
