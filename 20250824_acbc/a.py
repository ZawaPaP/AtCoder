X, Y = map(int, input().split())

month = X + Y

if month <= 12:
    print(month)
else:
    print(month - 12)
