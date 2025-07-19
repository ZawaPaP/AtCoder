C = [list(map(int, input().split())) for _ in range(3)]

for a_1 in range(101):
    b_1 = C[0][0] - a_1
    b_2 = C[0][1] - a_1
    b_3 = C[0][2] - a_1
    a_2 = C[1][0] - b_1
    a_3 = C[2][0] - b_1

    if a_2 + b_2 != C[1][1]:
        continue
    if a_2 + b_3 != C[1][2]:
        continue
    if a_3 + b_2 != C[2][1]:
        continue
    if a_3 + b_3 != C[2][2]:
        continue

    print("Yes")
    exit()
print("No")
