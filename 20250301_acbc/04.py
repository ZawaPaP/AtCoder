N, Q = map(int, input().split())


# map = {pigeon: nest}

pigeon_nest = {}
nest_map = [0]

for i in range(1, N + 1):
    pigeon_nest[i] = i
    nest_map.append(i)

for i in range(Q):

    query = list(map(int, input().split()))
    order = query[0]
    P = query[1]
    if order == 1:
        H = query[2]
        pigeon_nest[P] = nest_map[H]

    if order == 2:
        H = query[2]
        nest_a = P
        nest_b = H
        nest_map[P], nest_map[H] = nest_map[H], nest_map[P]

    if order == 3:
        for i in range(1, N + 1):
            if nest_map[i] == pigeon_nest[P]:
                print(i)
