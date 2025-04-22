N, Q = map(int, input().split())

A = list(map(int, input().split()))

count = 0

l = []

for _ in range(Q):
    l.append(list(map(int, input().split())))

for code in l:
    T, x, y = map(int, code)
    if T == 1:
        A[(x - 1 - count) % N], A[(y - 1 - count) % N] = (
            A[(y - 1 - count) % N],
            A[(x - 1 - count) % N],
        )
    if T == 2:
        count += 1
        count %= N
    if T == 3:
        print(A[(x - 1 - count) % N])
