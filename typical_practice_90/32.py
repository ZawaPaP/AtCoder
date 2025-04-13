# 区間がMax10のため、選手の走り方は最大でも10!通り
# 10! = 3628800 であり、全通りを計算しても時間内に解ける

# 選手の区間の選び方 N (N <= 10!)
# Nについて、時間を計算 & 仲が悪い走り方を除外

import itertools

N = int(input())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)


# 選手の走り方全通り
P = list(itertools.permutations(range(N)))


hate_map = {}

M = int(input())

for _ in range(M):
    x, y = map(int, input().split())

    # 選手を 0 ~ N - 1にする
    x -= 1
    y -= 1

    if hate_map.get(x):
        hate_map[x].append(y)
    else:
        hate_map[x] = [y]
    if hate_map.get(y):
        hate_map[y].append(x)
    else:
        hate_map[y] = [x]

ans = float("INF")

for permutate in P:
    prev = permutate[0]
    time = A[prev][0]
    valid = True
    for i in range(1, len(permutate)):
        if hate_map.get(prev) and permutate[i] in hate_map[prev]:
            valid = False
            break
        time += A[permutate[i]][i]
        prev = permutate[i]

    if valid:
        ans = min(ans, time)

if ans != float("INF"):
    print(ans)
else:
    print(-1)
