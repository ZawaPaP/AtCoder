N, T = map(int, input().split())

A = list(map(int, input().split()))

isOpen = True
count = 0
prev = 0
next_open = 0
for a in A:
    if isOpen:
        count += a
        isOpen = False
        next_open = a + 100

    else:
        if a < next_open:
            continue
        else:
            count += a - next_open
            next_open = a + 100

if next_open < T:
    count += T - next_open

print(count)
