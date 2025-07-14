H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]


def is_connected_with_black(i, j, S):
    DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for dir in DIRS:
        move_h = i + dir[0]
        move_w = j + dir[1]

        if move_h >= 0 and move_h < H and move_w >= 0 and move_w < W:
            if S[move_h][move_w] == "#":
                return True
    return False


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if not is_connected_with_black(i, j, S):
                print("No")
                exit()

print("Yes")
