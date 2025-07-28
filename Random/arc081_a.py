N = int(input())

A = list(map(int, input().split()))

d = {}

for a in A:
    d[a] = d.get(a, 0) + 1

sorted_d = sorted(d.items(), key=lambda x: x[0], reverse=True)

width = 0
height = 0
for k, v in sorted_d:
    if v <= 1:
        continue
    if v >= 4:
        if width == 0:
            width = k
            height = k
            break
        else:
            height = k
            break
    elif v >= 2:
        if width == 0:
            width = k
        else:
            height = k
            break
print(width * height)
