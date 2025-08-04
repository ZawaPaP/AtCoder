from collections import deque

H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]

marked = [[False] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            marked[i][j] = True

q = deque()
q.append([0, 0])

visited = [[False] * W for _ in range(H)]

while q:
    x, y = q.popleft()
    visited[x][y] = True

    if x == H - 1 and y == W - 1:
        if marked == visited:
            print("Possible")
            exit()
        else:
            print("Impossible")
            exit()

    under = [x + 1, y]
    right = [x, y + 1]

    if under[0] < H and A[under[0]][under[1]] == "#":
        q.append(under)
    if right[1] < W and A[right[0]][right[1]] == "#":
        q.append(right)

    if (
        under[0] < H
        and A[under[0]][under[1]] == "#"
        and right[1] < W
        and A[right[0]][right[1]] == "#"
    ):
        print("Impossible")
        exit()

print("Impossible")
