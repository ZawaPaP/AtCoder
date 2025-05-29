import math

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

last_order = ("", 0)

dishes = [A, B, C, D, E]

orders = []

for i in range(5):
    if dishes[i] % 10 == 0:
        order = dishes[i]
    else:
        order = math.ceil(dishes[i] / 10) * 10

    diff = order - dishes[i]
    if last_order[1] < diff:
        last_order = (i, diff)
    orders.append(order)

print(sum(orders) - last_order[1])
