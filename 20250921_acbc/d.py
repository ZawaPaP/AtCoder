T = int(input())

# idxからした1つ、右1つまでが重なっていたら重複を削除


def remove_duplicates(list):
    # 2x2の正方形で、最も重なりが大きい部分から消していく

    original_count = 0
    possible_idx = {}
    for idx in list:
        if possible_idx.get((idx[0], idx[1])) is None:
            possible_idx[(idx[0], idx[1])] = 0
        if possible_idx.get((idx[0] + 1, idx[1])) is None:
            possible_idx[(idx[0] + 1, idx[1])] = 0
        if possible_idx.get((idx[0], idx[1] + 1)) is None:
            possible_idx[(idx[0], idx[1] + 1)] = 0
        if possible_idx.get((idx[0] + 1, idx[1] + 1)) is None:
            possible_idx[(idx[0] + 1, idx[1] + 1)] = 0
        original_count += 1
        possible_idx[(idx[0], idx[1])] += 1
        possible_idx[(idx[0] + 1, idx[1])] += 1
        possible_idx[(idx[0], idx[1] + 1)] += 1
        possible_idx[(idx[0] + 1, idx[1] + 1)] += 1


def calc(grid):
    black_grid_lu_idx = []
    h, w = len(grid), len(grid[0])
    lu_idx = [0, 0]
    while True:
        if lu_idx[0] + 1 < h and lu_idx[1] + 1 < w:
            if grid[lu_idx[0]][lu_idx[1]] == '#' and grid[lu_idx[0] + 1][lu_idx[1]] == '#' and grid[lu_idx[0]][lu_idx[1] + 1] == '#' and grid[lu_idx[0] + 1][lu_idx[1] + 1] == '#':
                black_grid_lu_idx.append((lu_idx[0], lu_idx[1]))
            lu_idx[1] += 1
        elif lu_idx[1] + 1 >= w and lu_idx[0] + 1 < h:
            # 右に１マスしかない(縦長)
            lu_idx[0] += 1
            lu_idx[1] = 0
        else:
            break
    return remove_duplicates(black_grid_lu_idx)


ans = []
for _ in range(T):

    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    ans.append(calc(grid))

for a in ans:
    print(a)
