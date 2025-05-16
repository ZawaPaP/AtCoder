N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def count_diff(a, b):
    return sum(a[i][j] != b[i][j] for i in range(N) for j in range(N))


def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


rotations = [S]
for _ in range(3):
    rotations.append(rotate_90(rotations[-1]))

ans = min(count_diff(rotations[i], T) + i for i in range(4))
print(ans)
