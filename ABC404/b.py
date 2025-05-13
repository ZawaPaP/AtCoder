N = int(input())

S = []
T = []

for _ in range(N):
    row = list(input())
    S.append(row)

for _ in range(N):
    row = list(input())
    T.append(row)


# a, bで違うマス目の数をカウント
def count_diff(list_a, list_b):
    count = 0
    for i in range(N):
        for j in range(N):
            if list_a[i][j] != list_b[i][j]:
                count += 1

    return count


def rotate_90(lst):
    rotate = [["" for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotate[i][j] = lst[N - 1 - j][i]

    return rotate


rotate90 = rotate_90(S)
rotate180 = rotate_90(rotate90)
rotate270 = rotate_90(rotate180)

ans1 = count_diff(S, T)
ans2 = count_diff(rotate90, T)
ans3 = count_diff(rotate180, T)
ans4 = count_diff(rotate270, T)

ans = min(ans1, ans2 + 1, ans3 + 2, ans4 + 3)
print(ans)
