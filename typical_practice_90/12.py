from collections import deque


def isReachable(grids, start_r, start_c, goal_r, goal_c):
    if grids[start_r][start_c] == "w" or grids[goal_r][goal_c] == "w":
        return False

    r_length = len(grids)
    c_length = len(grids[0])

    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    Q = deque()
    Q.append([start_r, start_c])
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[start_r][start_c] = True

    while len(Q) != 0:
        node = Q.popleft()
        if node[0] == goal_r and node[1] == goal_c:
            return True

        for move in moves:
            next_r = node[0] + move[0]
            next_c = node[1] + move[1]

            if (
                0 <= next_r < r_length
                and 0 <= next_c < c_length
                and grids[next_r][next_c] == "r"
                and not visited[next_r][next_c]
            ):
                visited[next_r][next_c] = True
                Q.append([next_r, next_c])

    return False


H, W = map(int, input().split())

Q = int(input())

# 白を'w'とする
grids = [["w" for _ in range(W)] for _ in range(H)]

queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

for query in queries:
    if query[0] == 1:
        x = query[1] - 1
        y = query[2] - 1
        grids[x][y] = "r"
    if query[0] == 2:
        start_x = query[1] - 1
        start_y = query[2] - 1
        goal_x = query[3] - 1
        goal_y = query[4] - 1
        if isReachable(grids, start_x, start_y, goal_x, goal_y):
            print("Yes")
        else:
            print("No")
