m = int(input())

targets = [list(map(int, input().split())) for _ in range(m)]

n = int(input())
stars = []
for _ in range(n):
    x, y = map(int, input().split())
    stars.append((x, y))

stars_set = set(stars)

# targetsの1つを取り出して、starsの1つとのずれを計算する
# もしそれが並行移動後の座標であれば、targets全てが同じ量を並行移動した後の座標がstarsに含まれるはず

for star in stars:
    target = targets[0]
    diff = (star[0] - target[0], star[1] - target[1])
    # もし star がtargetの移動後であれば、他のtargetもstarsに存在
    isSameStar = True
    for i in range(1, m):
        moved = (targets[i][0] + diff[0], targets[i][1] + diff[1])
        if moved not in stars_set:
            isSameStar = False
            break
    if isSameStar:
        print(*diff)
        exit()
