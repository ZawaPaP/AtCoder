N, Q = map(int, input().split())
A = list(map(int, input().split()))

n = len(A)
moved = 0
for _ in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        x -= 1
        y -= 1
        x = (x - moved) % n
        y = (y - moved) % n
        A[x], A[y] = A[y], A[x]
    if T == 2:
        moved += 1
    if T == 3:
        x -= 1
        index = (x - moved) % n
        print(A[index])
