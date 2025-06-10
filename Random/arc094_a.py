A, B, C = map(int, input().split())

lst = [A, B, C]
lst.sort()

small = lst[0]
mid = lst[1]
big = lst[2]


ans = 0

while small < big and mid < big:
    small += 1
    mid += 1
    ans += 1

while small < mid:
    small += 2
    ans += 1

if small == mid:
    print(ans)
else:
    print(ans + 1)
