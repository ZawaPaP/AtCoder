N, Q = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(Q)]

card = [0] * N

for e in event:
    x = e[1]
    if e[0] == 1:
        card[x - 1] += 1
    elif e[0] == 2:
        card[x - 1] += 2
    else:
        if card[x - 1] >= 2:
            print("Yes")
        else:
            print("No")
