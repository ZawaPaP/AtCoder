N, S, T = map(int, input().split())

L = []
for _ in range(N):
    A, B, C, D = map(int, input().split())
    L.append((A, B, C, D))


# return length between 2 lines
# A,B,C,D are coordinates of 1 lines with A,B as start and C,D as end
def calc_lengths_between_lines(line1, line2):
    # length between line1's A,B and line2's A,B
    length1 = ((line1[0] - line2[0]) ** 2 + (line1[1] - line2[1]) ** 2) ** 0.5
    # length between line1's A,B and line2's C,D
    length2 = ((line1[0] - line2[2]) ** 2 + (line1[1] - line2[3]) ** 2) ** 0.5
    # length between line1's C,D and line2's A,B
    length3 = ((line1[2] - line2[0]) ** 2 + (line1[3] - line2[1]) ** 2) ** 0.5
    # length between line1's C,D and line2's C,D
    length4 = ((line1[2] - line2[2]) ** 2 + (line1[3] - line2[3]) ** 2) ** 0.5
    return min(length1, length2, length3, length4)


def calc_length_of_line(line):
    return ((line[0] - line[2]) ** 2 + (line[1] - line[3]) ** 2) ** 0.5


total_line_length = 0
for i in L:
    total_line_length += calc_length_of_line(i)


sum_length_between = 0
length_betweens = []
for i in range(N - 1):
    min_length_between = 10000
    length_between = []  # length_between[i] は、i番目の線と他の線の間の最短距離
    for j in range(i + 1, N):
        min_length_between = min(
            calc_lengths_between_lines(L[i], L[j]), min_length_between
        )
        length_between.append(min_length_between)
    length_betweens.append(length_between)


print(length_betweens)


total_time = total_line_length * T + sum_length_between * S
print(total_line_length * T)
print(sum_length_between * S)
print(total_time)
