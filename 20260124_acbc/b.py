Q = int(input())

isPaused = True
volume = 0
for _ in range(Q):
    a = int(input())
    if a == 1:
        volume += 1
    if a == 2:
        volume = max(volume - 1, 0)
    if a == 3:
        isPaused = not isPaused

    if volume > 2 and not isPaused:
        print("Yes")
    else:
        print("No")
