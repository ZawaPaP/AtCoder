N, R = map(int, input().split())
L = list(map(int, input().split()))

left_locks = L[:R]
right_locks = L[R:]

left_locks.reverse()
left_open_doors = left_locks.count(0)
right_open_doors = right_locks.count(0)


def calc_cost(locks, doors):
    opened = 0
    cost = 0
    for i in range(len(locks)):
        if opened == doors:
            return cost
        if locks[i] == 1:
            cost += 2
        else:
            cost += 1
            opened += 1
    return cost


# 片側だけで済む場合
if left_open_doors == 0 and right_open_doors == 0:
    print(0)
    exit()
elif left_open_doors == 0:
    cost = calc_cost(right_locks, right_open_doors)
    print(cost)
    exit()
elif right_open_doors == 0:
    cost = calc_cost(left_locks, left_open_doors)
    print(cost)
    exit()

else:
    left_cost = calc_cost(left_locks, left_open_doors)
    right_cost = calc_cost(right_locks, right_open_doors)

    print(left_cost + right_cost)
