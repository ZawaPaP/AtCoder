import math

N = int(input())

matrix = []
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

length = 0
length += math.sqrt(abs(matrix[0][0]) ** 2 + abs(matrix[0][1]) ** 2)
for i in range(N - 1):
    length += math.sqrt(
        abs(matrix[i][0] - matrix[i + 1][0]) ** 2
        + abs(matrix[i][1] - matrix[i + 1][1]) ** 2
    )

length += math.sqrt(abs(matrix[N - 1][0]) ** 2 + abs(matrix[N - 1][1]) ** 2)

print(length)
