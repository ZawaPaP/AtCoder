Q = int(input())

cards = []
for _ in range(Q):
    t, x = map(int, input().split())

    if t == 1:
        cards.insert(0, x)
    elif t == 2:
        cards.append(x)
    else:
        print(cards[x - 1])
