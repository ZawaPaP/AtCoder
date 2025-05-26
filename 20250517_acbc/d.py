H, W, N = map(int, input().split())

row_garbage = dict()
col_garbage = dict()

for _ in range(N):
    x, y = map(int, input().split())
    if x in row_garbage:
        row_garbage[x].add(y)
    else:
        row_garbage[x] = {y}

    if y in col_garbage:
        col_garbage[y].add(x)
    else:
        col_garbage[y] = {x}


ans = []

cleaned_row = dict()
cleaned_col = dict()

Q = int(input())
for _ in range(Q):
    order, pos = map(int, input().split())

    if order == 1:
        if pos not in row_garbage:
            ans.append(0)
            continue

        target = row_garbage[pos]
        for t in target:
            if t in cleaned_col:
                cleaned_col[t] += 1
            else:
                cleaned_col[t] = 1

        if pos in cleaned_row:
            ans.append(len(target) - cleaned_row[pos])
        else:
            ans.append(len(target))

        row_garbage.pop(pos)
    if order == 2:
        if pos not in col_garbage:
            ans.append(0)
            continue

        target = col_garbage[pos]
        for t in target:
            if t in cleaned_row:
                cleaned_row[t] += 1
            else:
                cleaned_row[t] = 1

        if pos in cleaned_col:
            ans.append(len(target) - cleaned_col[pos])
        else:
            ans.append(len(target))

        col_garbage.pop(pos)


for answer in ans:
    print(answer)
