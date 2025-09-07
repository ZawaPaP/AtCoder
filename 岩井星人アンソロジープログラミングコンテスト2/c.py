import re


H, W = map(int, input().split())

grid = []

for _ in range(H):
    temp = ""
    s = input()
    i = 0
    while i < len(s):
        if s[i] == '.':
            temp += s[i]
            i += 1
            continue
        if s[i] == '9':
            temp += "9Yiwiy"
            i += 6
            continue
        if s[i] == 'y':
            temp += "yiwiY9"
            i += 6
            continue
    grid.append(temp)


for g in grid:
    print(g)
