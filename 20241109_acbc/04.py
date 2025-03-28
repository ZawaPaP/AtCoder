Q = int(input())

Query = []
for _ in range(Q):
    Query.append(list(map(int, input().split())))

seed = 0
growth = []


def count_seed(array):
    total = 0
    for i in array:
        total += i[1]
    return total


for q in Query:
    if q[0] == 1:
        seed += 1

    if q[0] == 2:
        growth.insert(0, [q[1], seed])
        seed = 0

    if q[0] == 3:
        H = q[1]
        height = 0
        for i in range(len(growth)):
            if height + growth[i][0] >= H:
                print(count_seed(growth[i:]))
                growth = growth[:i]
                break

            else:
                height += growth[i][0]
