X, Y = map(int, input().split())


def rev(x, y):
    temp = str(x + y)
    return int(temp[::-1])


prevprev = X
prev = Y
temp = 0
for i in range(3, 11):
    temp = rev(prevprev, prev)
    prevprev = prev
    prev = temp

print(temp)
