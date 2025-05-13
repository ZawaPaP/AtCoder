from collections import deque

H, W = map(int, input().split())

C = []

for _ in range(H):
    row = list(input())
    C.append(row)


s_r = -1
s_c = -1

for i in range(H):
    for j in range(W):
        if C[i][j] == "s":
            s_r = i
            s_c = j
            break

visited = [([False] * W) for _ in range(H)]
visited[s_r][s_c] = True

stack = deque()
stack.append((s_r, s_c))

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
row_len = len(C)
col_len = len(C[0])

while stack:
    current_r, current_c = stack.pop()
    for direction in DIRS:
        next_r = current_r + direction[0]
        next_c = current_c + direction[1]

        if (
            0 <= next_r < row_len
            and 0 <= next_c < col_len
            and not visited[next_r][next_c]
            and C[next_r][next_c] != "#"
        ):
            if C[next_r][next_c] == "g":
                print("Yes")
                exit()
            stack.append((next_r, next_c))
            visited[next_r][next_c] = True

print("No")
