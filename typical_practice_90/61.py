from collections import deque

d = deque()

Q = int(input())

for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        d.appendleft(x)
    if t == 2:
        d.append(x)
    if t == 3:
        print(d[x - 1])
